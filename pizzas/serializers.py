from rest_framework import serializers
from .models import Topping, Pizza, Order
from django.utils import timezone
from decimal import Decimal

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.created_at:
            ret['created_at'] = timezone.localtime(instance.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return ret

class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True, read_only=True)
    topping_ids = serializers.PrimaryKeyRelatedField(queryset=Topping.objects.all(), many=True, write_only=True)
# To handle a Many-to-Many relationship with Topping model.
    class Meta:
        model = Pizza
        fields = '__all__'
        extra_kwargs = {
            'topping_ids': {'write_only': True}
        }

    def create(self, validated_data):
        toppings = validated_data.pop('topping_ids')
        pizza = Pizza.objects.create(**validated_data)
        pizza.toppings.set(toppings)
        return pizza

    def update(self, instance, validated_data):
        toppings = validated_data.pop('topping_ids')
        instance.toppings.set(toppings)
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.created_at:
            ret['created_at'] = timezone.localtime(instance.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return ret


class OrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    pizza_ids = serializers.PrimaryKeyRelatedField(queryset=Pizza.objects.all(), many=True, write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'pizza_ids': {'write_only': True}
        }

    def create(self, validated_data):
        pizzas = validated_data.pop('pizza_ids')
        order = Order.objects.create(**validated_data)
        order.pizzas.set(pizzas)
        return order

    def update(self, instance, validated_data):
        pizzas = validated_data.pop('pizza_ids')
        instance.pizzas.set(pizzas)
        return super().update(instance, validated_data)
    
    def calculate_total_price(self, instance):
        return sum(pizza.price for pizza in instance.pizzas.all())
    
    def calculate_discount(self, total_price, discount_percentage):
        return total_price * (Decimal(discount_percentage) / Decimal(100))
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.created_at:
            ret['created_at'] = timezone.localtime(instance.created_at).strftime('%Y-%m-%d %H:%M:%S')
        
        total_price = self.calculate_total_price(instance)
        discount_percentage = Decimal(10)  # Assume a fixed discount percentage for demonstration
        discount_amount = self.calculate_discount(total_price, discount_percentage)
        final_total_price = total_price - discount_amount
        
        ret['total_price'] = f'${total_price:.2f}'
        ret['discount_percentage'] = f'{discount_percentage}%'
        ret['discount_amount'] = f'${discount_amount:.2f}'
        ret['final_total_price'] = f'${final_total_price:.2f}'
        return ret