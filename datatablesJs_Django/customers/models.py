from django.db import models

# Create your models here.


class Customer(models.Model):
    AktifPasifType=(
    (0 , 'Aktif'),
    (1 , 'Pasif')
    )
    
    class Meta:
        db_table = 'Customer'
    
    hesapKodu = models.CharField(max_length=20,null=False, blank=False)
    unvan = models.CharField(max_length=80,null=False,blank=False)
    ad = models.CharField(max_length=40,null=True,blank=True)
    soyad = models.CharField(max_length=40,null=True,blank=True)
    aktifPasif = models.IntegerField(null=True,blank=True,choices=AktifPasifType)

    def __str__(self):
        return self.ad

    def to_dict_json(self):
        return{
            'id' : self.id,
            'hesapKodu' : self.hesapKodu,
            'unvan' : self.unvan,
            'ad' : self.ad,
            'soyad' : self.soyad,
            'aktifPasif' : self.aktifPasif,
            
        }
