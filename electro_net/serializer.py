from rest_framework import serializers

from electro_net.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'model', 'date_created')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'title', 'email', 'country', 'city', 'street', 'number_house',
                  'products', 'parent_supplier', 'time_created', 'debt_to_supplier', 'level')
        read_only_fields = ('level', 'debt_to_supplier',)
