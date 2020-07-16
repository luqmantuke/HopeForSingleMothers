from django.urls import path
from HFSM import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.BlogPageList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.detail, name='post_detail'),
    path('contact/', views.contact, name='contact')
]
