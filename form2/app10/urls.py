from django.urls import path
from app10 import views

urlpatterns=[
    path('',views.index,name='index'),
    # path('form',views.form_name_view,name='form_name')
    path('form',views.form,name='form'),
]