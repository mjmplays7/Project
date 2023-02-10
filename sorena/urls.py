from django.urls import path
from . import views

app_name = "sorena"
urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('admin/', views.admin, name="admin"),
    path('admin/login', views.login_view, name = "login"),
    path('admin/logout', views.logout_view, name = "logout"),
    path('schedule/', views.schedule, name = "schedule")
]
