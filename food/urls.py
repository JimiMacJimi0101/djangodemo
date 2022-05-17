from django.conf.urls import url
from django.urls import path
from food import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pst',views.pst,name='pst'),
]
