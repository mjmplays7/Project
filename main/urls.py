from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name = "index"),
    path('videos/', views.videos, name = "videos"),
    path('videos/<slug:slug>/', views.content, name = "content"),
    path('forms/', views.forms, name = "forms"),
    path('edu/', views.edu, name = "edu"),
    path('edu/<slug:slug>/', views.edu_content, name = "edu_content"),
    path('edu/c/<slug:slug>/', views.edu_course, name = "edu_course"),
    path('register/', views.register_view, name = "register"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('panel/', views.panel, name = "panel"),
    path('about/', views.about, name = "about")

]