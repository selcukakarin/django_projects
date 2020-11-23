from django import forms
from customers.models import Customer

class CustomerFormu(forms.ModelForm):

    class Meta:
        model = Customer

        fields = '__all__'
        widgets = {
            'hesapKodu': forms.TextInput(
                attrs={'id': 'hesapKodu', 'required': True}
            ),
            'unvan': forms.TextInput(
                attrs={'id': 'unvan'}
            ),
            'ad': forms.TextInput(
                attrs={'id': 'ad'}
            ),
            'soyad': forms.TextInput(
                attrs={'id': 'soyad'}
            ),
            'aktifPasif': forms.NumberInput(
                attrs={'id': 'aktifPasif', 'min':'0', 'value':'0'}
            ),
            
        }
