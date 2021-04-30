from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app1.forms import UserForm
from app1.models import User


def index(request):
    return HttpResponse("<h1>Welcome to app1. All /app1 urls are diverted to this app</h1>")


def about_us(request):
    return HttpResponse("<h1>This is App1. It is the app created within the DjangoProject</h1>")


@csrf_exempt
def user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = {
                'name': user_form.cleaned_data["name"],
                'email': user_form.cleaned_data["email"],
                'phone': user_form.cleaned_data["phone"],
                'dob': user_form.cleaned_data["dob"]
            }
            u1 = User(**user)
            u1.save()
            return render(request, "user_created.html", user)
    else:
        form = UserForm()
        return render(request, "add_user.html", {'form': form})


def show_user(request, name):
    # name = request.GET.get("name")
    try:
        user = User.objects.get(name=name)
        return render(request, "show_user.html", user.__dict__)
    except User.DoesNotExist:
        return HttpResponse(f"<h2>No user found with name: {name}</h2>")
