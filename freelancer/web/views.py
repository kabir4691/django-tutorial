from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'company_name': 'Freelancer'})

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
