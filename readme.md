- Pizza API with Authentication process
- The Steps:
    - Set up your Django project and app
    - Define the models
    - Create serializers
    - Create views
    - Define URLs
    - Test the API with Postman
    - Write tests

- Step 1: Set up your Django project and app
    - Install Django and Django REST framework
        - pip install django djangorestframework
    - Create a Django project
        - django-admin startproject pizza_market
        - cd pizza_market
    - Create a Django app
        - python manage.py startapp pizzas
    - Add the new app and REST framework to your INSTALLED_APPS in  pizza_market/settings.py:

        - INSTALLED_APPS = [
            'rest_framework',
            'pizzas',
        ]
- Step 2: Define the Models
    - In pizzas/models.py, define the models for your pizza market. For simplicity, let's assume we have three models: Pizza, Topping, and Order.
    - Run the migrations to create these models in the database:
        - python manage.py makemigrations
        - python manage.py migrate

- Step 3: Create Serializers
    - Create serializers for the models in pizzas/serializers.py

- Step 4: Create Views
    - Create views for the models in pizzas/views.py using Django REST framework's generic views

- Step 5: Define URLs
    - Define the URLs for the API in pizzas/urls.py
    - Include these URLs in the project's main urls.py  

- Step 6: Test the API with Postman
    - Run the Django development server   
    - Open Postman and test the API endpoints:

        Create a Topping: POST http://127.0.0.1:88888/api/toppings/ with a JSON body {"name": "Mushroom"}
        
        List Toppings: GET http://127.0.0.1:8888/api/toppings/
        
        Create a Pizza: POST http://127.0.0.1:8888/api/pizzas/ with a JSON body {"name": "Pepperoni", "price": 12.99, "toppings": [1]}
        
        List Pizzas: GET http://127.0.0.1:8888/api/pizzas/
        
        Create an Order: POST http://127.0.0.1:8888/api/orders/ with a JSON body {"customer_name": "John Doe", "address": "123 Main St", "pizzas": [1]}
        
        List Orders: GET http://127.0.0.1:8888/api/orders/


- Step 7: Write Tests
    - In pizzas/tests.py, write tests for your API
    

- Noteeeeeeee
  - All ports in the endpoints are 8888, remember that.
