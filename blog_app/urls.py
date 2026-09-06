from django.shortcuts import render,get_object_or_404
from django.urls import path
from . import views

urlpatterns =[
    path('<int:c_id>/',views.post_by_category , name='post_by_category')
]