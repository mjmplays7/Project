from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, "sorena/index.html")

def info(request):
    if request.method == "POST":
        name = request.POST['name']
        last = request.POST['last']
        number = request.POST['number']
        national_id = request.POST['national_id']
        birthyear = request.POST['birthyear']
        birthmonth = request.POST['birthmonth']        
        birthday = request.POST['birthday']
        start_insurance_year = request.POST['start_insurance_year']
        start_insurance_month = request.POST['start_insurance_month']
        start_insurance_day = request.POST['start_insurance_day']
        
        user = Sorena_User(name=name, last=last, number=number,national_id=national_id, birthyear=birthyear, birthmonth=birthmonth, birthday=birthday, start_insurance_year=start_insurance_year, start_insurance_month=start_insurance_month, start_insurance_day=start_insurance_day)
        user.save()
    
        return HttpResponseRedirect(reverse('sorena:info'))
    return render(request, "sorena/info.html")


def about(request):
    return render(request, "sorena/about.html")

def admin(request):
    try:
        Admin.objects.get(username=request.user)
    except Admin.DoesNotExist:
        return HttpResponse("وارد حساب کاربری مجاز شوید")
    admin = Admin.objects.get(username=request.user)
    if not request.user.is_authenticated or not admin: 
        return HttpResponseRedirect(reverse('sorena:login'))

    Sorena_Users = Sorena_User.objects.all()
    list = []
    for user in Sorena_Users:
        date = int(user.start_insurance_year + 1)
        list.append(date)
    return render(request, 'sorena/admin.html', {
        "Sorena_Users": Sorena_Users,
        "date": list
    })
   


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user:
            admin_usernames = Admin.objects.all()
            for admin_username in admin_usernames:
                if username == admin_username.username:
                    login(request, user)
                    return HttpResponseRedirect(reverse('sorena:admin'))

        else:
            return render(request, 'sorena/login.html', {
                "message": "اطلاعات وارد شده اشتباه است"
            })

    return render(request, "sorena/login.html")    

def logout_view(request):
    logout(request)
    return render(request, 'sorena/login.html',{
        "message": "خارج شدید"
    })








