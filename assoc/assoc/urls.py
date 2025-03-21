"""assoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from createassoc import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.test, name='nn'),
    path('', views.tofirstpage, name='fp'),
    path('participant', views.addparticipant, name='addpart'),
    path('consultation', views.consultation, name='cons'),
    path('tombola/<str:hex_code>/', views.tombola, name='tombola'),
    path('waitting', views.waitting, name='wtn'),
    path('consultation_sk', views.consultation1, name="fin")
]
