from django.db import models

# Create your models here.,


class Currency(models.Model):
    """Parabirimlerini muhafaza etmek için model. Ör: USD, TL, EUR"""
    code = models.CharField(max_length=10)  # USD
    name = models.CharField(max_length=100)  # United States Dollar
    is_active = models.BooleanField(default=False)  #
    is_base_currency = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 't_currency'  # veritabanında bu modelin tablo adı


class CurrencyRate(models.Model):
    """Parabirimleri arasındaki  oranları muhafaza etmek için model."""
    currency = models.ForeignKey(Currency,
                                 related_name="currency_rate",
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    base_currency = models.ForeignKey(Currency,
                                      on_delete=models.CASCADE,
                                      blank=True, null=True)

    rate = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_currency_rate'


class BasicUnit(models.Model):
    """Kilogram, liter etc.."""
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 't_basic_unit'

    def __str__(self):
        return self.code


class Supplier(models.Model):
    """Tedarikçi için model"""
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    address = models.TextField()

    class Meta:
        db_table = 't_supplier'

    def __str__(self):
        return self.name


class MaterialStock(models.Model):
    """Hammadde Stok için model"""
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=False)
    stock_name = models.CharField(max_length=140, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    basic_unit = models.ForeignKey(BasicUnit,
                                   on_delete=models.SET_NULL,
                                   blank=True, null=True)
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)

    class Meta:
        db_table = 't_material_stock'
