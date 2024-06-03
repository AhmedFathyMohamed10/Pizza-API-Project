from django.urls import path
from .views import ToppingListCreate, ToppingDetail, PizzaListCreate, PizzaDetail, OrderListCreate, OrderDetail

urlpatterns = [
    path('toppings/', ToppingListCreate.as_view(), name='topping-list-create'),
    path('toppings/<int:pk>/', ToppingDetail.as_view(), name='topping-detail'),
    path('pizzas/', PizzaListCreate.as_view(), name='pizza-list-create'),
    path('pizzas/<int:pk>/', PizzaDetail.as_view(), name='pizza-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
