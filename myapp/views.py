from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    print(posts)
    return render(request, "myapp/home.html", context)

def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("new_post")

    context = {
        "form" : form,
    }
    return render(request, "myapp/new_post.html", context)