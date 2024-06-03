from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .def_permissions import IsAuthenticatedAndOwner
from .models import Topping, Pizza, Order
from .serializers import ToppingSerializer, PizzaSerializer, OrderSerializer

class ToppingListCreate(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    permission_classes = [AllowAny]

class ToppingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    permission_classes = [AllowAny]

class PizzaListCreate(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

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

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedAndOwner]  
