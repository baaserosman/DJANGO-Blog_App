from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
#! /////////////// READ //////////////

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, "myapp/home.html", context)


def detail(request,id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post" : post
    }
  
    return render(request, "myapp/detail.html", context)


def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created succesfully.")
            return redirect("home")

    context = {
        "form" : form,
    }
    return render(request, "myapp/new_post.html", context)

def post_update(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    print(form)
 
    if request.method == "POST" :
        form = PostForm(request.POST, request.FILES,  instance=post)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("home")
    
    context = {
        "form" : form,
    }
    return render(request, "myapp/post_update.html", context)

def post_delete(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST" :
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("home")
    
    return render(request, "myapp/post_delete.html")