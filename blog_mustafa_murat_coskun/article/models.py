from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    #models.CASCADE bağlı olunan auth.User tablosundaki  #user'ımız silinirse o user'a ait article'larında silinmesini sağlar
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="yazar")      
    title=models.CharField(max_length=50,verbose_name="başlık")
    content=RichTextField()
    date = models.DateTimeField(verbose_name="Herhangi bir tarih")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    article_image=models.FileField(blank=True,null=True,verbose_name="Makaleye fotoğraf ekleyin")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    #yukarıdaki kodda related_name özelliği bizim ileride Article.comments ile bu Article'a bağlı commentlere de ulaşabilmemizi sağlayacaktır.
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True )
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
    # sıralama tarihte son yapılan yorum ilk gösterilir