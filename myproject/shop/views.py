from django.http import HttpResponse

def home(request):
    return HttpResponse("shop Home Page")

def products(request):
    return HttpResponse("shop products Page")