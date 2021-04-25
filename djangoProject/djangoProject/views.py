import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>This is the index page</h1>")


def about(request):
    return HttpResponse("""
    <html><body bgcolor='red'>
    <h2><B>Bodacious</> is the best in Jaipur</h2>
    </body></html>""")


def show_one(request):
    with open("resource/one.txt", "r") as f1:
        return HttpResponse("<h2> %s </h2>" % f1.read())


def form(request):
    return render(request, "form.html", {})


def confirm(request):
    name = request.GET.get("txtname")
    age = request.GET.get("txtage")
    is_graduate = "a graduate" if request.GET.get("chkgraduate") else "not a graduate"
    salary = request.GET.get("txtsalary")
    hra = request.GET.get("txthra")
    ta = request.GET.get("txtta")
    da = request.GET.get("txtda")
    total = int(salary) + int(hra) + int(ta) + int(da)
    param_dict = {
        "name": name,
        "age": age,
        "is_graduate": is_graduate,
        "salary": salary,
        "hra": hra,
        "ta": ta,
        "da": da,
        "total": total
    }
    return render(request, "view_form.html", param_dict)


def input_file(request):
    return render(request, "write_file.html", {})


def write_file(request):
    fname = request.GET.get("txtfname")
    fcontent = request.GET.get("txtfcontent")
    if "txt" != fname.split('.')[-1]:
        fname += ".txt"
    fpath = "resource/" + fname
    with open(fpath, "w") as f1:
        f1.write(fcontent)
    return HttpResponse(f"<h2>{fname} written successfully...</h2>")


def last_login_cookie(request):
    if request.COOKIES.get("last_login"):
        last_login = request.COOKIES.get("last_login")
        response = HttpResponse(f"<h2>Your last login was at {last_login}.</h2>")
    else:
        response = HttpResponse(f"<h2>This is your first login.</h2>")
    response.set_cookie("last_login", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return response


def login_session(request):
    if request.session.has_key("user"):
        name = request.session["user"]
        city = request.session["city"]
        return HttpResponse(f"<h2>Hi {name} from {city}, welcome back</h2>")
    else:
        return render(request, "login.html", {})


def session_saved(request):
    name = request.GET.get("txtname")
    city = request.GET.get("txtcity")
    request.session["user"] = name
    request.session["city"] = city
    return HttpResponse(f"<h2>Hi {name} from {city}, your session have been created!!</h2>")


# will need to set email_id and email_password in env variables for code to run
def create_mail(request):
    return render(request, "send_mail.html", {})


def send_email(request):
    subject = request.GET.get("txtsubject")
    message = request.GET.get("txtmessage")
    from_emil = settings.EMAIL_HOST_USER
    to = request.GET.get("txtto")
    recipient_list = [to]
    send_mail(subject=subject, message=message, from_email=from_emil, recipient_list=recipient_list)
    return HttpResponse(f"<h2>Mail Sent to {to}</h2>")
