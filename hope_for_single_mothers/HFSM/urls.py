from django.urls import path
from HFSM import views


urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog')
]
