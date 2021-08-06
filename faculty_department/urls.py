from django.contrib import admin
from django.urls import *
from .import views

urlpatterns=[

path('',views.home,name="home"),
path('export_excel',views.export_excel,name="export_excel")

]