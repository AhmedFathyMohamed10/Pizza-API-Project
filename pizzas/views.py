from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .def_permissions import IsAuthenticatedAndOwner
from .models import Topping, Pizza, Order
from .serializers import ToppingSerializer, PizzaSerializer, OrderSerializer

from drf_yasg.utils import swagger_auto_schema # type: ignore

class ToppingListCreate(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_description="Get a list of all toppings or create a new topping")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new topping")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ToppingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a topping by ID")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a topping by ID")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a topping by ID")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class PizzaListCreate(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(operation_description="Get a list of all pizzas or create a new pizza")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new pizza")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a pizza by ID")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a pizza by ID")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a pizza by ID")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        # Ensure the user creating the order is set as the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Filter orders to only show the ones belonging to the authenticated user
        return self.queryset.filter(user=self.request.user)
    
    @swagger_auto_schema(operation_description="Get a list of orders for the authenticated user or create a new order")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new order for the authenticated user")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedAndOwner]  

    @swagger_auto_schema(operation_description="Retrieve, update, or delete an order by ID for the authenticated user")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an order by ID for the authenticated user")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete an order by ID for the authenticated user")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
