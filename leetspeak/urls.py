from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("api/<str:string>", views.api, name="api"),
    path("examples/", views.examples, name="examples")
]
