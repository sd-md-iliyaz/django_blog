from django.shortcuts import get_object_or_404, render,redirect
from blog_app.models import Category,Blog
from django.contrib.auth.decorators import login_required 
from .forms import CategoryForm,PostForm
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    c_count =Category.objects.all().count()
    b_count =Blog.objects.all().count()
    context = {
        'c_count':c_count,
        'b_count':b_count
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')
def add_category(request):
    if request.method == "POST" :
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    
    form=CategoryForm()
    context = {
        'form':form,
    }
    return render(request,"dashboard/add_category.html",context)

def edit_category(request,c_id):
    category=get_object_or_404(Category,pk=c_id)
    if request.method == "POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
        
    form=CategoryForm(instance=category)
    context = {
            'form':form,
            'c_id':category,
        }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,c_id):
    category=get_object_or_404(Category,pk=c_id)
    category.delete()
    return redirect("categories")

def posts(request):
    posts=Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'dashboard/post.html',context)
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug=slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        
    form=PostForm()
    
    return render(request,'dashboard/add_post.html',{'form':form})
def edit_post(request,c_id):
    post=get_object_or_404(Blog,pk=c_id)
    if request.method == "POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug=slugify(title)+ '-' + str(post.id)
            post.save()
            return redirect("posts")
    form=PostForm(instance=post)
    context={
        'form':form,
        'post':post,
    }
    return render(request,'dashboard/edit_post.html',context)
def delete_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')