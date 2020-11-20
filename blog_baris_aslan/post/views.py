from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def postIndex(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
                                        Q(title__icontains=query) |
                                        Q(content__icontains=query) |
                                        Q(user__first_name__icontains=query) |
                                        Q(user__last_name__icontains=query)
                                     ).distinct()

    paginator = Paginator(post_list, 2)  
    
    page_number = request.GET.get('sayfa')
    posts = paginator.get_page(page_number)

    return render(request, 'post/index.html', {'posts': posts})


def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', context)


def postCreate(request):

    if not request.user.is_authenticated:
        return Http404

    # if request.method == "POST":
    #     print(request.POST)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title, context=context)

    # if request.method == "POST":
    #     # Formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    # else:
    #     # Formu kullanıcıya göster
    #     form = PostForm()
    #

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Başarılı bir şekilde post oluşturuldu.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def postUpdate(request, slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        post = form.save()
        messages.success(request, 'Başarılı bir şekilde post güncellendi.', extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def postDelete(request, slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')