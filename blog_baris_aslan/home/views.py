from django.shortcuts import render, HttpResponse

# Create your views here.

def homeView(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Selçuk'
        }
    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'home.html', context)