from django import forms
from .models import Article     #Article modelimizi import ediyoruz

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model=Article       # Formumuzla Article modelimizi bağladık
        fields=["title","content","article_image","date"]
        