from django.urls import path
from . import views

urlpatterns = [
    path("",views.userlogin,name="login"),
    path("registration/",views.userregistration,name="registration"),
    path("userhomepage/",views.userhome,name="home"),
    path("adminhomepage/",views.webadmin,name="webadmin"),
    path("logout/",views.logout_view,name="logout"),
]