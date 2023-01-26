
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    contents = Content.publish.all()[:4]
    videos = Video.publish.all()[:4]
    return render(request, "main/index.html", {
        "contents": contents,
        "videos": videos
    })

def videos(request):
    #video = Video.objects.filter(status = "published")
    videos = Video.publish.all()
    return render(request, "main/videos.html", {
        "videos": videos
    })

def content(request, slug):
    video = Video.publish.get(slug = slug)
    return render(request, "main/content.html", {
        "video": video
    })

def forms(request):
    return render(request, "main/forms.html")

def edu(request):
    contents = Content.publish.all()
    return render(request, "main/edu.html", {
        "contents": contents
    })

def edu_content(request, slug):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, "main/login.html", {
                "message": "برای خرید محتوا وارد حساب کاربری خود شوید"
            })
        content = Content.publish.get(slug=slug)
        try:
            Main_User.objects.get(username=request.user, bought=content.id) 
        except Main_User.DoesNotExist: 
                
            try:
                User_Order.objects.get(username=request.user)
            except User_Order.DoesNotExist:
                order = User_Order(username=request.user, order=content.id)
                order.save()
                return HttpResponseRedirect("/go-to-gateway/")
            User_Order.objects.filter(username=request.user).update(order=content.id)
            return HttpResponseRedirect("/go-to-gateway/")
       
        
        return render(request, "main/edu_course.html", {
            "content": content
        })


    content = Content.publish.get(slug = slug)
    return render(request, "main/edu_overview.html", {
        "content": content
    })

def edu_course(request, slug):
    if not request.user.is_authenticated:
            return render(request, "main/login.html", {
                "message": "برای مشاهده محتوا وارد حساب کاربری خود شوید"
            })
    content = Content.publish.get(slug=slug)
    try:
        Main_User.objects.get(username=request.user, bought=content.id) 
    except Main_User.DoesNotExist:
        return render(request, "main/edu_overview.html", {
            "content": content
        })
    return render(request, "main/edu_course.html", {
        "content": content
    })


def register_view(request):
    if request.method == 'POST':
        try: 
            User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            if not request.POST['password'] == request.POST['re_password']:
                return render(request, "main/register.html", {
                    "message": "رمز و تکرار آن یکی نیست"
                })
            if not len(request.POST['password']) > 7:
                return render(request, "main/register.html", {
                    "message": "طول رمز شما کمتر از 8 رقم است"
                })
            if request.POST['password'] == request.POST['username']:
                return render(request, "main/register.html", {
                    "message": "رمز شما خیلی شبیه به نام کاربری است"
                })    
            if not len(request.POST['number']) == 11:
                return render(request, "main/register.html", {
                    "message": "شماره تلفن اشتباه است"
                })    
            name = request.POST['name']
            last = request.POST['last']
            email = request.POST['email']
            number = request.POST['number']
            username = request.POST['username']
            password = request.POST['password']

            user = User(first_name=name, last_name=last, email=email, username=username, password=password)
            user.save()
            if not User.objects.get(username=request.POST['username']):
                return render(request, "main/register.html", {
                    "message": "ثبت نشد لطفا اطلاعات را برسی کنید و رمز قوی انتخاب کنید"
                })
            return HttpResponseRedirect(reverse('main:panel'))
        return render(request, "main/register.html", {
                "message": "نام کاربری قبلا استفاده شده است لطفا یکی دیگر انتخاب کنید"
            })

    return render(request, "main/register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)

            return HttpResponseRedirect(reverse('main:panel'))
        else:
            return render(request, 'main/login.html', {
                "message": "اطلاعات اشتباه است"
            })

    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'main/login.html',{
        "message": "از حساب خود خارج شدید"
    })
def panel(request):
    if not request.user.is_authenticated: 
        return HttpResponseRedirect(reverse('main:login'))
    return render(request, "main/panel.html")