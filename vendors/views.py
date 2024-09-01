from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        return queryset

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        po = self.get_object()
        po.acknowledgment_date = timezone.now()
        po.save()
        self.update_vendor_metrics(po.vendor)
        return Response({'status': 'Purchase order acknowledged'})

    def perform_create(self, serializer):
        po = serializer.save()
        self.update_vendor_metrics(po.vendor)

    def perform_update(self, serializer):
        po = serializer.save()
        self.update_vendor_metrics(po.vendor)

    def update_vendor_metrics(self, vendor):
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_pos = completed_pos.count()

        if total_completed_pos > 0:
            # On-Time Delivery Rate
            on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now()).count()
            vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100

            # Quality Rating Average
            quality_ratings = completed_pos.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
            if quality_ratings:
                vendor.quality_rating_avg = sum(quality_ratings) / len(quality_ratings)

            # Fulfilment Rate
            fulfilled_pos = completed_pos.filter(status='completed', quality_rating__isnull=False).count()
            vendor.fulfillment_rate = (fulfilled_pos / total_completed_pos) * 100

        # Average Response Time
        acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor).exclude(acknowledgment_date__isnull=True)
        if acknowledged_pos.exists():
            response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos]
            vendor.average_response_time = sum(response_times) / len(response_times)

        vendor.save()
