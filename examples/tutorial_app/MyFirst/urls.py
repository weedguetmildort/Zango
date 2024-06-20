"""
URL configuration for MyFirst project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('MyFirstApp.urls')),
]

handler400 = 'MyFirstApp.views.custom_400_view'
handler403 = 'MyFirstApp.views.custom_403_view'
handler404 = 'MyFirstApp.views.custom_404_view'
handler500 = 'MyFirstApp.views.custom_500_view'
handler502 = 'MyFirstApp.views.custom_502_view'


