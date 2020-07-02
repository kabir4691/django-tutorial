from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog.html', {'company_name': 'Freelancer'})

def article(request, blog_id):
    return render(request, 'article.html', {'company_name': 'Freelancer', 'blog_id': blog_id})