from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, PurchaseOrder
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils import timezone
import json

class VendorManagementTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='dhruv', password='1234')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test St',
            vendor_code='TEST001'
        )

    def test_create_vendor(self):
        url = reverse('vendor-list')
        data = {
            'name': 'New Vendor',
            'contact_details': 'new@example.com',
            'address': '456 New St',
            'vendor_code': 'NEW001'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_get_vendor_performance(self):
        url = reverse('vendor-performance', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('on_time_delivery_rate', response.data)
        self.assertIn('quality_rating_avg', response.data)
        self.assertIn('average_response_time', response.data)
        self.assertIn('fulfillment_rate', response.data)

    def test_create_purchase_order(self):
        url = reverse('purchaseorder-list')
        data = {
            'po_number': 'PO001',
            'vendor': self.vendor.id,
            'order_date': timezone.now().isoformat(),
            'delivery_date': (timezone.now() + timezone.timedelta(days=7)).isoformat(),
            'items': json.dumps({'item1': 'description1'}),  # Convert dict to JSON string
            'quantity': 5,
            'status': 'pending',
            'issue_date': timezone.now().isoformat()
        }
        response = self.client.post(url, data, format='json')  # Specify format as JSON
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_acknowledge_purchase_order(self):
        po = PurchaseOrder.objects.create(
            po_number='PO002',
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=7),
            items={'item2': 'description2'},
            quantity=3,
            status='pending',
            issue_date=timezone.now()
        )
        url = reverse('purchaseorder-acknowledge', kwargs={'pk': po.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        po.refresh_from_db()
        self.assertIsNotNone(po.acknowledgment_date)
