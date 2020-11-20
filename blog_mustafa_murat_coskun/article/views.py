from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,reverse
from .forms import ArticleForm      #Şuanki klasörümüzün içindeki forms dosyasından ArticleForm'u aldık
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})

    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

# Create your views here.
def index(request):
    context={  
        "number1":10,
        "number2":20
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
#@login_required decorator'ı aşağıdaki fonksiyon ile gidilen sayfanın sadece giriş yapıldıysa görüntülenmesini sağlar
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)
#@login_required decorator'ı aşağıdaki fonksiyon ile gidilen sayfanın sadece giriş yapıldıysa görüntülenmesini sağlar
@login_required(login_url="user:login")
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)  

    if form.is_valid():
        article=form.save(commit=False)     #############  article'ın author bilgisi olmadan kaydedilmemesi için henüz veritabanına commit etme dedik.
        article.author=request.user
        article.save()          #commit=True olur ve vt'ye article kaydedilir.

        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")
    
    return render(request,"addArticle.html",{"form":form})

def detail(request,id):
    # article=Article.objects.filter(id=id).first()       #.first yazmaz isek bir queryset dönmekte.
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()
    #modelimizde commet sınıfımızdaki fk'nın related_name özelliğine comments dediğimiz için article'ın tüm commentlerine ulaşabiliriz. comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})


#@login_required decorator'ı aşağıdaki fonksiyon ile gidilen sayfanın sadece giriş yapıldıysa görüntülenmesini sağlar
@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)   #instance parametresine buradaki objeyi gönderirsek objedeki bilgiler article formunun içine yazılır
    #yani instance formun dolu gelmesini sağlar
    if form.is_valid():
        article=form.save(commit=False)     #############  article'ın author bilgisi olmadan kaydedilmemesi için henüz veritabanına commit etme dedik.
        article.author=request.user
        article.save()          #commit=True olur ve vt'ye article kaydedilir.

        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})
#@login_required decorator'ı aşağıdaki fonksiyon ile gidilen sayfanın sadece giriş yapıldıysa görüntülenmesini sağlar
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()

    messages.success(request,"Makale başarıyla silindi")
    return redirect("article:dashboard")

def addComment(request,id):
    article=get_object_or_404(Article,id = id)

    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))
    # reverse fonksiyonu dinamik bir url yönlendirmek için kullanılıyor
    # örnekte kwargs ile dinamik olarak id mizi yolladık ve istediğimiz sayfaya yönlendirme yaptık 

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple.html')