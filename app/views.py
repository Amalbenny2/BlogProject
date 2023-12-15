
from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import BlogPostForm

def latest_blog_posts(request):
    latest_posts = BlogPost.objects.order_by('-pub_date')[:5]
    return render(request, 'latest_posts.html', {'latest_posts': latest_posts})




def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latest_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})