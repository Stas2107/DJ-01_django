from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('data', views.data),
    path('test', views.test),
    path('create_news', views.create_news, name='add_news')
]