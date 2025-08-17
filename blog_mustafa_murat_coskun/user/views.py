from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm 
from django.contrib import messages         #Django uyarı mesajları için gerekli kütüphane
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout          # authenticate user login işlemlerinin kontrolü için kullanılır

# Create your views here.

def register(request):
    # Eğer POST gelirse form dolu oluşturulur. Eğer GET request gelirse form boş oluşur
    form=RegisterForm(request.POST or None)

    #form.is_valid() metodu forms.py'deki clean() metodunu çağırır
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        

        return redirect("index")
        
    context={
        "form":form
    }
    return render(request,"register.html",context)

    """
    # sayfaya get request mi post request mi olduğunu anlarız
    if request.method=="POST":
        #post request olursa posttan gelen veriler ile formumuzu doldururuz
        form=RegisterForm(request.POST)
        #form.is_valid() metodu forms.py'deki clean() metodunu çağırır
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            return redirect("index")
        
        context={
            "form   ":form
        }
        return render(request,"register.html",context)
    else:
        #get request olursa boş form oluştururuz
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)
        """
def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        #eğer formumuzda clean metodu tanımlamadıysak django kendisi otomatik olarak tanımlar aşağıdaki kullanımda örneklendirdik
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)    #authenticate username ve password var ise user oluşturur yoksa None döner
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")

