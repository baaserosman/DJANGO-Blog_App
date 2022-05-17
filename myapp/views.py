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
    print(posts)
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
            return redirect("home")

    context = {
        "form" : form,
    }
    return render(request, "myapp/new_post.html", context)