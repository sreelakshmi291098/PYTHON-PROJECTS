from django.urls import path
from app12 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('users',views.users,name='users')
    
]