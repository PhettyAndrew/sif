from django.urls import path
from . import views
from . models import ShowImages

app_name = 'appSigtuna'

urlpatterns=[
    path('',views.index,name='index'),
    path('team',views.team,name='team'),
    path('news',views.news,name='news'),
    path('gallery',views.gallery,name='gallery'),
]