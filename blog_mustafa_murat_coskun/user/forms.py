from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı adı ")
    password=forms.CharField(label="Parola ",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı ")
    password=forms.CharField(max_length=20,label="Parola ",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Parolayı doğrula ",widget=forms.PasswordInput)
    
    #clean metodunun içindeki if yapısı ile iki alan aynı ise formu submit eder, değilse submit etmez
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmedi")

        values={
            "username":username,
            "password":password,
        }
        return values