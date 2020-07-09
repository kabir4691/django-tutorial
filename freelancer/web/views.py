from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {'company_name': 'Freelancer'})

def contact(request):
    data = json.loads(request.body)
    # print(json.loads('{"name": "Arkesh"}'))
    # print(json.loads(request.body))
    contact = Contact(
        name = data["name"],
        email = data["email"],
        phone = data["phone"],
        message = data["message"]
    )
    contact.save()
    return JsonResponse({
        'success': True,
        'message': 'Your query has been recorded. We will get in touch with you shortly.',
        'data': data
    }, json_dumps_params={'indent': 2})