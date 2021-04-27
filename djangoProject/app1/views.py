from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to app1. All /app1 urls are diverted to this app</h1>")


def about_us(request):
    return HttpResponse("<h1>This is App1. It is the app created within the DjangoProject</h1>")
