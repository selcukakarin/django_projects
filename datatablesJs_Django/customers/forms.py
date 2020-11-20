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
            'field1': forms.NumberInput(
                attrs={'id': 'field1', 'min':'0', 'value':'0'}
            ),
            'field2': forms.NumberInput(
                attrs={'id': 'field2', 'min':'0', 'value':'0'}
            ),
            'field3': forms.TextInput(
                attrs={'id': 'field3'}
            ),
            'field4': forms.TextInput(
                attrs={'id': 'field4'}
            ),
            'field5': forms.TextInput(
                attrs={'id': 'field5'}
            ),
            'field6': forms.TextInput(
                attrs={'id': 'field6'}
            ),
            'field7': forms.TextInput(
                attrs={'id': 'field7'}
            ),
            'field8': forms.TextInput(
                attrs={'id': 'field8'}
            ),
            'resim': forms.TextInput(
                attrs={'id': 'resim'}
            ),
            'field10': forms.TextInput(
                attrs={'id': 'field10'}
            ),
            'field11': forms.TextInput(
                attrs={'id': 'field11'}
            ),
            'field12': forms.TextInput(
                attrs={'id': 'field12'}
            ),
            'field13': forms.NumberInput(
                attrs={'id': 'field13', 'min':'0', 'value':'0'}
            ),
            'field14': forms.NumberInput(
                attrs={'id': 'field14', 'min':'0', 'value':'0'}
            ),
            'field15': forms.TextInput(
                attrs={'id': 'field15'}
            ),
            'field16': forms.CheckboxInput(
                attrs={'id': 'field16'}
            ),
            'field17': forms.CheckboxInput(
                attrs={'id': 'field17'}
            ),
            'field18': forms.TextInput(
                attrs={'id': 'field18'}
            ),
            'field19': forms.CheckboxInput(
                attrs={'id': 'field19'}
            ),
            'field20': forms.EmailInput(
                attrs={'id': 'field20'}
            ),
            'field21': forms.TextInput(
                attrs={'id': 'field21'}
            ),
            'field22': forms.EmailInput(
                attrs={'id': 'field22'}
            ),
            'field23': forms.EmailInput(
                attrs={'id': 'field23'}
            ),
            'field24': forms.EmailInput(
                attrs={'id': 'field24'}
            ),
            
        }
