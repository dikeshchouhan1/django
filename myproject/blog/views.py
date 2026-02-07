from django.http import HttpResponse

def home(request):
    return HttpResponse("blog Home Page")

def about(request):
    return HttpResponse("blog about Page")