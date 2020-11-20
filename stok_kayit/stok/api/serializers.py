from rest_framework import serializers
# internal
from stok.models import Supplier, MaterialStock


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # fields = '__all__'
        fields = ('id', 'name', 'phone', 'email', 'address')


class StockSerializer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source="supplier.name")
    currency_code = serializers.ReadOnlyField(source="currency.code")
    unit_code = serializers.ReadOnlyField(source="basic_unit.code")

    class Meta:
        model = MaterialStock
        fields = '__all__'


class StockCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialStock
        fields = '__all__'


class StockListSerializer(serializers.ModelSerializer):
    # ID olarak gösterilen alanlar override edilerek name ve code gösterimi yapıldı
    supplier_name = serializers.ReadOnlyField(source="supplier.name")
    currency_code = serializers.ReadOnlyField(source="currency.code")
    unit_code = serializers.ReadOnlyField(source="basic_unit.code")

    url = serializers.HyperlinkedIdentityField(view_name='api-stock-detail', lookup_field='pk')

    class Meta:
        model = MaterialStock
        fields = '__all__'

