"""tms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views,views1
urlpatterns = [
#     django administration url
    path('admin/', admin.site.urls),
#     url for landing page
    path('loginpage/',views.loginpage,name='loginpage'),
#     url for login function
    path('login/',views.login,name='login'),
#     url for main page
    path('main/',views.main,name='main'),
#     urls for apis
    path('TrafficAtA/',views1.ListTrafficAtA.as_view()),
    path('TrafficAtB/',views1.ListTrafficAtB.as_view()),
    path('TrafficAtC/',views1.ListTrafficAtC.as_view()),
    path('TrafficAtD/',views1.ListTrafficAtD.as_view()),
    path('LatestTrafficAtA/',views1.ListLatestTrafficAtA.as_view()),
#     url for logout
    path('logout/',views.logout,name='logout'),
    
#     path('manual/',views.manualoveride,name="manual"),
    path('automate/',views.automate,name="automate"),
]
