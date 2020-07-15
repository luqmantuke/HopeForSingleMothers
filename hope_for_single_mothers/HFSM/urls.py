from django.urls import path
from HFSM import views


urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.BlogPageList.as_view(), name='blog'),
    path('<slug:slug>/', views.detail, name='post_detail'),

]
