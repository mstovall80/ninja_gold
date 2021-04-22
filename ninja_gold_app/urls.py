from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path("", views.index),
    path("process_money", views.process_money),
    path('reset', views.reset)
]