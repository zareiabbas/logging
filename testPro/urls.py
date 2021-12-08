from django.contrib import admin
from django.urls import path
from logApp.views import sayHello

urlpatterns = [path('admin/', admin.site.urls), path('sayHello/', sayHello)]
