from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
    "title": title,
    }
    return render(request, "home.html",context)


def article_entry(request):
    title = 'Add Article'
    form = ArticleForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('article:article_list')
    context = {
    "title": title,
    "form": form,
    }
    return render(request, "article_entry.html",context)


def article_list(request):
     title = 'List of all computers'
     queryset = Article.objects.all()
     context = {
         "title": title,
         "queryset": queryset,
     }
     return render(request, "article_list.html",context)
