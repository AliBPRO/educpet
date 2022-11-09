from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http.response import JsonResponse
from .models import *

# Create your views here.
def index(request):
	context = locals()
	template = 'index.html'
	return render(request, template, context)

def send_information_email(request):
	sujet = "Demande site : " + request.POST.get('name')
	email_client = request.POST.get('email')
	message = request.POST.get('message') + "\n\nEmail du client : " + email_client
	
	email = EmailMessage(sujet, message, to=['educpet@gmail.com'])
	email.send()

	return JsonResponse({},status=200)


def boutique(request):
	list_categorie = Categorie.objects.all()
	
	context = locals()
	template = 'boutique.html'
	return render(request, template, context)

def mention_legale(request):
	context = locals()
	template = 'mentions_legales.html'
	return render(request, template, context)
