from django import forms
from .models import Article
 
class ArticleForm(forms.ModelForm):
   any_date = forms.DateField(
      widget=forms.DateInput(attrs={
        'class': 'dateinput',
      }),
      error_messages={'invalid': 'your custom error message'}
    )
   class Meta:
      model = Article
      fields = ['title', 'any_date']
   