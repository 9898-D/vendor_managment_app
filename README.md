**Vendor Management System**

This is a Django-based Vendor Management System that allows users to manage vendor profiles, track purchase orders, and calculate vendor performance metrics. The project also includes an API built using Django REST Framework (DRF).

**Requirements**

Python 3.8+
Django 5.1+
Django REST Framework
PostgreSQL or SQLite (for local development)
Git (for version control)
Virtualenv (recommended)

**Setup Instructions
Follow these steps to set up the project on your local system:**

**1. Clone the Repository**
git clone https://github.com/9898-D/vendor_managment_app.git
cd vendor_managment_app

**2. Create a Virtual Environment**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**3. Install Dependencies**
pip install -r requirements.txt

**5. Apply Migrations**

python manage.py makemigrations
python manage.py migrate

**6. Create a Superuser**
Create a superuser to access the Django admin interface:

python manage.py createsuperuser

**7. Start the Development Server**
python manage.py runserver

**Running the Project**

Admin Interface: http://127.0.0.1:8000/admin/
API Root: http://127.0.0.1:8000/api/

**API Authentication**
To access the API endpoints, you'll need to authenticate using a token. You can generate a token by making a POST request to the /api-token-auth/ endpoint with your credentials.
API Endpoint: http://127.0.0.1:8000/api-token-auth/

**API Endpoints**

Below are some of the key API endpoints available in the project:

Vendor List & Create:           GET/POST /api/vendors/
Vendor Detail & Update:         GET/PATCH/PUT/DELETE /api/vendors/<int:pk>/
Purchase Order List & Create:   GET/POST /api/purchase_orders/
Purchase Order Detail & Update: GET/PATCH/PUT/DELETE /api/purchase_orders/<int:pk>/
Vendor Performance:             GET /api/vendors/<int:pk>/performance/

**Running Tests**
python manage.py test

This will execute the test suite and provide output on any test failures or errors.

**8. Testing the API**
A Postman collection is included in the repository, covering all the API endpoints from token generation to vendor management. You can import this collection into Postman and use it to test the APIs.

Generate Token: Start by generating a token using the /api-token-auth/ endpoint.
Vendor Management: Use the provided endpoints to create, retrieve, update, and delete vendors.
Purchase Order Management: Manage purchase orders through the API.
Vendor Performance: Evaluate vendor performance using the provided endpoint.


**9. Import Postman Collection**

**1.  Generate the Token**  
  >  API ENDPOINT : http://127.0.0.1:8000/api-token-auth/
  >  METHOD : POST
  >  BODY:  {
              "username": "USER_NAME",
              "password": "PASSWORD"
            }


**2. CREATE A VENDOR**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/
  >  METHOD : POST
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  {
              "name": "Vishal",
              "contact_details": "986798861",
              "address": "Address 6",
              "vendor_code": "V0016"
            }

**3. CREATE A PURCHASE ORDER**
  >  API ENDPOINT : http://127.0.0.1:8000/api/purchase_orders/
  >  METHOD : POST
  > HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json 
  >  BODY:  {
              "po_number": "V001",
              "vendor": 2,  // Replace with the actual vendor ID you received from the previous step
              "order_date": "2024-09-27T12:00:00Z",
              "delivery_date": "2024-09-01T12:00:00Z",
              "items": {"item3": 50, "item4": 200},
              "quantity": 200,
              "status": "completed",
              "issue_date": "2024-09-25T12:00:00Z"
            }

**4. UPDATE A VENDOR**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/1/
  >  METHOD : PUT
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  {
              "name": "Dhruv choubisa",
              "contact_details": "7227098861",
              "address": "Address 2 Hello World",
              "vendor_code": "D002"  
            }

**5. UPDATE A PURCHASE ORDER**
  >  API ENDPOINT : http://127.0.0.1:8000/api/purchase_orders/1/
  >  METHOD : PATCH
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  {
              "status": "completed",
              "quality_rating": 5.0
            }

**6. RETRIEVE VENDORS BY ID**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/1
  >  METHOD : GET
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json 
  >  BODY:  NO REQUIRED

**7. RETRIEVE PURCHASE ORDER BY ID**
  >  API ENDPOINT : http://127.0.0.1:8000/api/purchase_orders/1/
  >  METHOD : GET
  >  BODY:  NO REQUIRED

**8. DELETE VENDOR**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/2/
  >  METHOD : DELETE
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  NO REQUIRED

**9. DELETE PURCHASE ORDER**
  >  API ENDPOINT : http://127.0.0.1:8000/api/purchase_orders/1/
  >  METHOD : DELETE
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  NO REQUIRED

**10. RETRIEVE ALL VENDORS**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/
  >  METHOD : GET
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  NO REQUIRED

**11. RETRIEVE ALL PURCHASE ORDER**
  >  API ENDPOINT : http://127.0.0.1:8000/api/purchase_orders/
  >  METHOD : GET
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  NO REQUIRED

**12. RETRIEVE ALL PURCHASE ORDER**
  >  API ENDPOINT : http://127.0.0.1:8000/api/vendors/1/performance/
  >  METHOD : GET
  >  HEADERS: KEY                  Value
              Authorization        Token {generate_token}
              Content-Type         application/json
  >  BODY:  NO REQUIRED










