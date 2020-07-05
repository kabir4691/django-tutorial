from django.shortcuts import render
from .models import Post

# Create your views here.
freelancer_blog = Post.objects.all()

def index(request):
    return render(request, 'blog.html', {'company_name': 'Freelancer', 'blog': freelancer_blog})

def post(request, post_id):
    print(freelancer_blog[post_id-1])
    return render(request, 'post.html', {'company_name': 'Freelancer', 'post': freelancer_blog[post_id-1]})