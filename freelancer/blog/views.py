from django.shortcuts import render
from .models import Post

# Create your views here.
freelancer_blog = []
freelancer_blog.append(Post())
freelancer_blog[0].id = 1
freelancer_blog[0].title = 'Why Python?'
freelancer_blog[0].content = 'Lorem ipsum dolor sit amet...'
freelancer_blog[0].author = 'Ankur'
freelancer_blog[0].date = '2020-07-04'
freelancer_blog.append(Post())
freelancer_blog[1].id = 2
freelancer_blog[1].title = 'My First Django Project'
freelancer_blog[1].content = 'Lorem ipsum dolor sit amet (2)...'
freelancer_blog[1].author = 'Kabir'
freelancer_blog[1].date = '2020-07-08'

def index(request):
    return render(request, 'blog.html', {'company_name': 'Freelancer', 'blog': freelancer_blog})

def post(request, post_id):
    return render(request, 'post.html', {'company_name': 'Freelancer', 'post': freelancer_blog[post_id-1]})