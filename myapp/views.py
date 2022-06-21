from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Like, PostView, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from .utils import get_random_code
from django.template.defaultfilters import slugify



def home(request):
    posts = Post.objects.filter(status="p")
    context = {
        'posts':posts
    }
    return render(request, "myapp/home.html", context)

@login_required()
def new_post(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            code = slugify(form.instance.title + " " + get_random_code())
            form.instance.slug = code
            post = form.save(commit=False)
            post.author = request.user            
            post.save()
            messages.success(request, "Post created succesfully.")
            return redirect("home")
    context = {
        "form" : form,
    }
    return render(request, "myapp/new_post.html", context)

def detail(request, slug):
    # comment = Comment.objects.all( )
    # who = request.user
    form = CommentForm()
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    if request.method == 'POST' :
        form =CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("detail", slug=slug)

    context = {
        "post" : post,
        "form" : form,
    }
  
    return render(request, "myapp/detail.html", context)

@login_required()
def post_update(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.user.id != post.author.id:
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not a writer of this post!")
        return redirect("home")
 
    if form.is_valid():
        # form.instance.author = request.user
        # code = slugify(form.instance.title + " " + get_random_code())
        # form.instance.slug = code
        form.save()
        messages.success(request, "Post updated.")
        return redirect("home")
    
    context = {
        "form" : form,
        "post" :post,
    }
    return render(request, "myapp/post_update.html", context)

@login_required()
def post_delete(request,slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.id != post.author.id:
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not a writer of this post!")
        return redirect("home")

    if request.method == "POST" :
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("home")
    
    return render(request, "myapp/post_delete.html")


@login_required()
def like(request,slug) :
    if request.method == "POST" :
        post = get_object_or_404(Post, slug=slug)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like[0].delete()
        else :
            Like.objects.create(user=request.user, post=post)
        return redirect("detail", slug=slug)
    return redirect("detail", slug=slug)

