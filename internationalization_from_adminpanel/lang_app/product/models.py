from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    name = models.CharField(_('Product Name'), max_length=140, null=True, blank=True)
    title = models.CharField('Ürün Başlığı', max_length=140, null=True, blank=True)
    price = models.DecimalField('Ürün Fiyatı', max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
        ordering = ('-created_at',)