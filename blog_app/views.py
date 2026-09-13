from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q

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

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    if request.method == "POST":
        comment=Comment()
        comment.user = request.user
        comment.blog=single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments=Comment.objects.filter(blog=single_blog)
    comment_count=Comment.objects.all().count()
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs= Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) )
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)