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
    field1 = models.IntegerField(null=True,blank=True)
    field2 = models.IntegerField(null=True,blank=True)
    field3 = models.CharField(max_length=20,null=True,blank=True)
    field4 = models.CharField(max_length=20,null=True,blank=True)
    field5 = models.CharField(max_length=20,null=True,blank=True)
    field6 = models.CharField(max_length=20,null=True,blank=True)
    field7 = models.CharField(max_length=20,null=True,blank=True)
    field8 = models.CharField(max_length=20,null=True,blank=True)
    resim = models.ImageField(null=True,blank=True, default = 'default.jpg')
    field10 = models.CharField(max_length=20,null=True,blank=True)
    field11 = models.CharField(max_length=20,null=True,blank=True)
    field12 = models.CharField(max_length=20,null=True,blank=True)
    field13 = models.IntegerField(null=True,blank=True)
    field14 = models.IntegerField(null=True,blank=True)
    field15 = models.CharField(max_length=20,null=True,blank=True)
    field16 = models.BooleanField(null=True,blank=True,default=False)
    field17 = models.BooleanField(null=True,blank=True,default=False)
    field18 = models.CharField(max_length=20,null=True,blank=True)
    field19 = models.BooleanField(null=True,blank=True,default=False)
    field20 = models.EmailField(max_length=50,null=True,blank=True)
    field21 = models.CharField(max_length=50,null=True,blank=True)
    field22 = models.EmailField(max_length=50,null=True,blank=True)
    field23 = models.EmailField(max_length=50,null=True,blank=True)
    field24 = models.EmailField(max_length=50,null=True,blank=True)

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
            'field1' : self.field1,
            'field2' : self.field2,
            'field3' : self.field3,
            'field4' : self.field4,
            'field5' : self.field5,
            'field6' : self.field6,
            'field7' : self.field7,
            'field8' : self.field8,
            'resim' : str(self.resim),
            'field10' : self.field10,
            'field11' : self.field11,
            'field12' : self.field12,
            'field13' : self.field13,
            'field14' : self.field14,
            'field15' : self.field15,
            'field16' : self.field16,
            'field17' : self.field17,
            'field18' : self.field18,
            'field19' : self.field19,
            'field20' : self.field20,
            'field21' : self.field21,
            'field22' : self.field22,
            'field23' : self.field23,
            'field24' : self.field24
        }
