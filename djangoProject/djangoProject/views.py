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
