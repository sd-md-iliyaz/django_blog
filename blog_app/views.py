from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Blog,Category

# Create your views here.
def post_by_category(request,c_id):
    posts = Blog.objects.filter(category=c_id).order_by('-updated_at')
    try:
        category=Category.objects.get(pk=c_id)
    except:
        return redirect('404.html')
    context={
        'posts' : posts,
        'c_id' : category,
    }
    return render(request , 'post_by_category.html',context)