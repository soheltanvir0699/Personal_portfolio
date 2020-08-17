from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('', views.all_blogs, name='all_blogs'),

]
