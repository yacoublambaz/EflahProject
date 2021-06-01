from django.contrib import admin
from django.urls import path
from . import views

"""

    path('logout/', views.logout, name = "logout"),
    
    path('join/',views.joinRequest,name="join"),
    """
urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', views.loginView,name="loginView"),
    path('signup/',views.signupView, name="signup"),
    path('postRequest/',views.postRequest, name="postRequest"),
    ]

