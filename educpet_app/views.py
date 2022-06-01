from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http.response import JsonResponse


# Create your views here.
def index(request):
	context = locals()
	template = 'index.html'
	return render(request, template, context)

def send_information_email(request):
	print(request)
	sujet = "Demande site : " + request.POST.get('name')
	email_client = request.POST.get('email')
	message = request.POST.get('message') + "\n\nEmail du client : " + email_client
	
	email = EmailMessage(sujet, message, to=['educpet@gmail.com'])
	print(email)
	print(email.send())
	email.send()
	print(email)

	return JsonResponse({},status=200)
