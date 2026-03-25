from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('endereco/<int:id>', views.endereco,name="endereco"), 
    path('', list_address, name='list_address'),
    path('create/', create_address, name='create_address'),
    path('update/<int:id>/', update_address, name='update_address'),
    path('delete/<int:id>/', delete_address, name='delete_address')
 
]

