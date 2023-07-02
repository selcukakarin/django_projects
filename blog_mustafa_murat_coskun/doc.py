#### ÖNEMLİ DJANGO KOMUTLARI ####
#model'ları json formatında listeler
python manage.py dumpdata --format json -- indent 4
# products model'ını json formatında listeler
python manage.py dumpdata products --format json -- indent 4
# products model'ını json formatında  fixtures klasörüne kaydeder
python manage.py dumpdata products --format json -- indent 4 > products(anadizindeki klasör ismi)/fixtures/products.json



#git önceki versiyona dönme işlemi
git log
git checkout <gitlogdan dönen karakter dizini> -- .    <------ nokta koyarsak projenin tamamı gelir. nokta yerine dosya ismi yazrsak sadece o dosyanın önceki versiyonu gelir

#git ssh işlemleri
1- Uç birim terminal ekranını açıyoruz.

2- Aşağıdaki satırdaki kodu yapıştırıp enter tuşuna basıyoruz.

ssh-keygen -t rsa -b 4096 -C "eposta@adresiniz.com"

3- Bu aşamada SSH anahtarının bulunduğu dosyanın nereye kaydedileceğini soruyor. Özel konum istemiyorsanız enter tuşuna basabilirsiniz. SSH için dizin oluşturulacaktır.
4- Bir anahtar kelime belirlememizi istiyor. Belirtmek istemiyorsanız enter tuşuna basarak geçebilirsiniz.
İşlem sonucunda dosya belirlediğiniz dizinde oluşturulur.
5- Şimdi sıra geldi SSH anahtar kodumuzu ekrana yazdırmaya. Bunun için şu komutu veriniz:

cat ~/.ssh/id_rsa.pub
Kodu fareyle seçtikten sonra kopyala deyin.

Haydi bu kodu GitLab hesabımıza ekleyelim. 
6- GitLab.com 1 'da oturum açıyoruz.

7- Profil menüsünden Settings’e tıklıyoruz.
8- SSH Keys 'e tıklıyoruz.
9- Form’a hafızadaki kodu yapıştırıyoruz. Ardından Add key tuşuna basıyoruz.
SSH kodunu GitLab’a tanıttık.

10- Şimdi işlemin başarıyla gerçekleşip gerçekleşmediğini test edelim.

Uçbirim Terminal ekranında şu komutu verelim.

ssh -T git@gitlab.com


#python kurulum
sudo apt-get install -y python3.7.2
alias python=python3
python --version

#pip kurulum
sudo apt install python3-pip

#Virtual environment install
sudo apt-get install python3-venv
python3 -m venv myvenv
source myvenv/bin/activate
deactivate

#postgresql kurulumu
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo apt-get --purge remove postgresql
dpkg -l | grep postgres
sudo apt-get --purge remove postgresql postgresql-doc postgresql-common

#pgadmin4 kurulumu
sudo apt-get install postgresql-11 pgadmin4

#postgresql servis başlatma
sudo service postgresql start

#postgresql işlemleri
sudo su - postgres
psql
CREATE DATABASE LNKCLOUDERP;
CREATE USER linkuser WITH PASSWORD 'linkpassword123';
ALTER ROLE linkuser SET client_encoding TO 'utf8';
ALTER ROLE linkuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE linkuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE LNKCLOUDERP TO linkuser;
\q
exit

#psycopg2 veritabanımızda değişikliğe izin veriyor.
pip install django psycopg2


#Django kurulumu

__init__.py myapp klasörünün bir python dosyası olduğunu gösterir
settings.py ayarlarımızı bulunduran dosya
urls.py site yönlendirme (map ayarları) işlemleri yapılır.

pip3 install Django==2.1.7
pip3 install -U Django==2.1.7
python3 -m django --version
pip3 uninstall Django

#proje oluşturma kodu
django-admin.py startproject linkerp

#Django projemizi local hostta çalıştırıyoruz
python3 manage.py runserver
    
#Database ayarlarını settings.py dosyasından yapabiliriz
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lnkclouderp',
        'USER': 'linkuser',
        'PASSWORD': 'linkpassword123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#setting.py deki değişiklikleri veritabanına yansıtmak için kullanılan komutlar
python manage.py makemigrations #ilk defa oluşturulan tablolar için 
python manage.py migrate  #app'lerimiz içindeki veritabanları oluşturulur

#admin sayfasına bağlanmak için pgadmin4 üzerinden bir server tanımlaması yapmamız gerekli.

#superuser oluşturuyoruz
python manage.py createsuperuser

#uygulama oluşturma kodu
python manage.py startapp erpDb

#Article model oluşturma ve Admin arayüzüne ekleme
#models.py
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=models.TextField(verbose_name="İçerik")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")

#admin.py modelimizi admin panelimize kayıt ediyoruz
from .models import Article

# Register your models here.
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #Article sayfasında hangi özelliklerin gösterileceğini seçmek için
    list_display=["title","author","created_date","content"]

    #Article sayfasında hangi özelliklerin link alacağını belirler
    list_display_links=["title","author","created_date"]

    #Article sayfasında title'a göre arama özelliği geldi
    search_fields=["title"]

    #Article sayfasında sağ köşede bir süzgeç menü oluşturulur.
    #list_filter=["content"]
    list_filter=["title"]

    #Meta class'ı python'ın bize önerdiği bir classtır. ismi değiştirilemez. model=Article yardımıyla Article ile ArticleAdmini bağlar.
    class Meta:
        model=Article

#myapp/setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "article",
]

#Django Shell ile ORM sorgularını kullanma
#Shell ekranımızı açıyoruz interactive console
python manage.py shell

#Djangonun için bulunan hazır User modelini import ediyoruz
from django.contrib.auth.models import User

#Bizim oluşturduğumuz Article modelini de import ediyoruz
from article.models import Article

#User modelinden newUser nesnemizi türetiyoruz ve server'ımıza ekliyoruz
newUser=User(username="userselcuk",password="123")
newUser.save()

#Diğer tanımlama methodları
>>> newUser2=User(username="alikullanici")
>>> newUser2.set_password("123")
>>> newUser2.save()
>>> newUser3=User()
>>> newUser3.username=("mustikullanici")
>>> newUser3.set_password("123")
>>> newUser3.first_name="musti"
>>> newUser3.save()

#Article modelimizden article nesnemizi tanımlıyoruz 
>>> article=Article(title="Django Shell Deneme",content="İçerik",author=newUser3)
>>> article.save()

#Diğer tanımlama yöntemleri
>>> article2=Article()
>>> article2.title="deneme 15"
>>> article2.content="İçerik"
>>> article2.author=newUser3
>>> article2.save()
>>> Article.objects.create(title="Deneme 21",content="21",author=newUser2)
<Article: Deneme 21>
>>> article=Article.objects.create(title="Yazı Başlık",content="Yazı içerik",author=newUser2)
>>> article.title
'Yazı Başlık'
>>> article.title="Yazı Başlık Değişti"
>>> article.save()

#Article nesnelerimizi çekiyoruz
>>> Article.objects.all()
<QuerySet [<Article: 1>, <Article: 2>, <Article: 3>, <Article: Django Shell Deneme>, <Article: deneme 15>, <Article: Deneme 21>, <Article: Yazı Başlık Değişti>]>

#title'ı "Django Shell Deneme" olan article'ı çekiyoruz
>>> article=Article.objects.get(title="Django Shell Deneme")
>>> article.title
'Django Shell Deneme'

#article'ı siliyoruz
>>> article.delete()
(1, {'article.Article': 1})

#Article'larımız görünüyor
>>> Article.objects.all()
<QuerySet [<Article: 1>, <Article: 2>, <Article: 3>, <Article: deneme 15>, <Article: Deneme 21>, <Article: Yazı Başlık Değişti>]>
#id değeri 1 olan article'ımızı alıyoruz
>>> article=Article.objects.get(id=1)
>>> article
<Article: 1>
>>> article.delete()
>>> Article.objects.all()
<QuerySet [<Article: 2>, <Article: 3>, <Article: deneme 15>, <Article: Deneme 21>, <Article: Yazı Başlık Değişti>]>

#__contains komutu ile içerisinde "en" geçen article'larımızı sorguluyoruz
>>> Article.objects.filter(title__contains="en")
<QuerySet [<Article: deneme 15>, <Article: Deneme 21>]>

#Template(html dosyalarımızı) templates klasörü altında tutmak için uygulamamız olan myapp/settings.py dosyasına aşağıdaki kodu ekliyoruz
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"], #Artık html sayfalarımızın yolu templates klasörü olabilir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Eğer "" yani localhost url'imiz için HttpResponse yani bir string göndermek ister isek aşağıdaki gibi yaparız
#önce views.py'de bir method yazarız
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h3> Anasayfa </h3>")

#daha sonra myapp/urls.py ye şunları ekleriz
from django.contrib import admin
from django.urls import path
from article.views import index ###

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.

]

#eğer HttpResponse yerine bir html dönmek istersek aşağıdaki kodu uygularız
return render(request,"index.html")

#static file(css,js vs) kullanımı

#settings.py'ye eklenmeli
STATIC_URL = '/static/'


#app'imiz içindeki static file'ımızı kullanabilmek için
{% load static %}
<img src="{% static "my_app/example.jpg" %}" alt="My image"/>

<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Selçuk Site</title>
    <link rel="stylesheet" href="{% static "style.css" %}">
</head>
<body>
    <h3>Anasayfa</h3>
    <p>Design by Selçuk Akarın</p>
</body>
</html>

#eğer static dosyalarımızı app'lerimiz içinde değil de projemiz içinde tanımlamak istersek settings.py dosyasına eklenir
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Selçuk Site</title>
    <link rel="stylesheet" href="{% static "style.css" %}">
</head>
<body>
    <h3>Anasayfa</h3>
    <p>Design by Selçuk Akarın</p>
</body>
</html>

#uygulamamıza (app) özel bir urls.py tanımlamak için 
#myproject/urls.py dosyasına aşağıdaki gibi tanımlama yapmalıyız
from django.contrib import admin
from django.urls import path,include
from article import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.
    path('about/', views.about,name="about"),
    path('detail/<int:id>', views.detail,name="detail"), # dinamik url tanımlama için
    path('article/',include("article.urls")),

]
#app'imizdeki tanımlama aşağıdaki gibi olmalı
from django.contrib import admin
from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('create/',views.index,name="index"),
]

#bir register formu tasarlıyoruz
from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı: ")
    password=forms.CharField(max_length=20,label="Parola: ",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Parolayı Doğrula: ",widget=forms.PasswordInput)
    #clean metodu bize parolaların kontrolünü sağlayıp giriş yapılıp yapılmayacağı konusunda bize yetki verir
    #clean metodu sadece views.py'de form.is_valid() fonksiyonu yardımıyla çağrılır
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        values={
            #burada hangi key ile döndüysek views'da yine username=form.cleaned_data.get("username") bu şekilde yakalamamız gerek
            "username":username,
            "password":password
        }
        return values

#register.html'e bir form oluşturuyoruz
{% extends "layout.html" %}
{% block body %}
<h3>Kayıt Ol!</h3>
<hr>
<form method="post">
    {% csrf_token %} <!--Cross in the middle attacklarına karşı korumayı sağlayan bir kod-->
    {{form.as_p}}
    <br>
    <button type="submit" class="btn btn-danger">Kayıt Ol</button>
</form>
{% endblock body %}

#user/urls.py dosyamıza aşağıdaki eklemeleri yapıyoruz
from django.contrib import admin
from django.urls import path
from . import views   

app_name="user"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),

]

#myproject/urls.py aşağıdaki gibi düzenlenir
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"), #localhost:8000 adresimize gideriz. article/views.py dosyamızdaki index methodunu çalıştırırız.
    path('about/', views.about,name="about"),
    path('detail/<int:id>', views.detail,name="detail"), # dinamik url tanımlama için
    path('article/',include("article.urls")), #article/...
    path('user/',include("user.urls")), #user/register user/...


]

#user/views.py de aşağıdaki işlemler yapılır
from django.shortcuts import render,redirect # yönlendirme işlemi için redirect'i import ettik
from .forms import RegisterForm
from django.contrib import messages #django mesajlarını kullanabilmek için
from django.contrib.auth.models import User #user modelinden nesne oluşturmak için import ediyoruz
from django.contrib.auth import login # login yapabilmek için import ediyoruz

# Create your views here.

def register(request):
    #request post ise formdaki bilgilerle form oluşturulur
    #request get ise boş bir form oluşur
    form=RegisterForm(request.POST or None)
    if form.is_valid(): #parolalarımızın eşleşip eşleşmediğini kontrol ediyoruz
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save() #kullanıcı bilgilerini alıp veritabanımıza kayıt ediyoruz
        login(request,newUser) # giriş yapıyoruz
        messages.success(request,"Başarıyla kayıt oldunuz") #kayıt olduğuna dair layout.html sayfasına başarı mesajı iletiyoruz

        

        return redirect("index") #anasayfaya yönlendiriyoruz
        #post request olsa bile parolalar eşleşmiyor ise aynı sayfayı geri dönüyoruz
    context={
        "form":form
    }
    return render(request,"register.html",context)

    """
    if request.method=="POST": #metodumuzun post olma durumunu kotrol ediyoruz
        form=RegisterForm(request.POST) #post ise post'tan gelen verileri form değişkenine alıyoruz
        if form.is_valid(): #parolalarımızın eşleşip eşleşmediğini kontrol ediyoruz
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save() #kullanıcı bilgilerini alıp veritabanımıza kayıt ediyoruz
            login(request,newUser) # giriş yapıyoruz
            return redirect("index") #anasayfaya yönlendiriyoruz
        #post request olsa bile parolalar eşleşmiyor ise aynı sayfayı geri dönüyoruz
        context={
            "form":form
        }
        return render(request,"register.html",context)

    else:
        #eğer bir sayfa yenilemesi olduysa yani get request olduysa formumuzu boş döndürüyoruz
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)
    """

    """form=RegisterForm()
    context={
        "form":form
    }
    return render(request,"register.html",context)
    """
def loginUser(request):
    return render(request,"login.html")
def logoutUser(request):
    pass


#danger message
<div style="margin-top:100px;" class="container">
        {% if messages %}
           
                <!-- aşağıdaki yapı ile djangoda olmayan danger mesajını kullanabiliriz-->
                {% for message in messages %}
                <!-- <div{% if message.tags %} class="alert alert-{{ message.tags }}"{% endif %}>{{ message }}</div> -->
                {% if message.tags == "info" %}
                <div class="alert alert-danger">{{ message }}</div>
                {% else %}
                <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                {% endif %}
                {% endfor %}
            
        {% endif %}
        {% block body %}
        
        {% endblock  %}

    </div>

#crispy formları kullanmak için
pip install --upgrade django-crispy-forms
#hata vermesi durumunda 
pip3 install --user django-crispy-forms

#setting.py için
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#login.html aşağıdaki gibi düzenlenmeli

{% extends "layout.html" %}
{% block body %}
{% load crispy_forms_tags %}


<div class="row">
  <div class="col-md-6 offset-md-3">
    <h3>Giriş yap</h3>
    <hr>

    <form method="post">
    {% csrf_token %}
    {{form|crispy}}
    <br>
    <button type="submit" class="btn btn-danger">Giriş yap</button>

    </form>

  </div>
</div>


{% endblock body %}

#dinamik url yapısı
<a class="navbar-brand" href="{% url 'index' %}">LinkErp</a>   <!-- dinamik url yapısı kullanıldı -->
<li class="nav-item active">
    <a class="nav-link" href="{% url 'erpDb:dashboard' %}">Kontrol Paneli <span class="sr-only">(current)</span></a>
</li>

# Form'ların tasarımını aldığı Models'ta alanların alabileceği farklı parametreler
#dropdownbox
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
title = models.CharField(max_length=3, choices=TITLE_CHOICES)


python3 manage.py migrate --fake erpDb zero
python3 manage.py migrate erpDb


### Projeye ckeditor ekleme için aşağıdaki adımlar takiğ edilir tek fark duruma göre pip3 ile yapılır
https://github.com/django-ckeditor/django-ckeditor

## FileUpload
# Python da ImageField özelliğini kullanabilmek için aşağıdaki yüklme yapılır
pip3 install Pillow

# daha sonra FileUpload için aşağıdaki adımlar takip edilir
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

# django Clean_Up uygulaması örneğin bir makalemiz silindiği anda o makaleye bağlı resimlerinde silinmesini sağlar
#Kurulumu
https://pypi.org/project/django-cleanup/
pip3 install django-cleanup



