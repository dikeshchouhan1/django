from django.http import HttpResponse

def post_details(request ,post_id):
    return HttpResponse(f"<h1> show blog post{post_id}</h1>")
def post_profile(request ,username):
    return HttpResponse(f"<h1> show blog post{username}</h1>")
