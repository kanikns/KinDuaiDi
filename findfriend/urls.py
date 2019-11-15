from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:friend_id>/', views.detail, name='friend_detail')
]