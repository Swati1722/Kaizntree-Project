from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('', views.home),
    path('login/', views.handle_login),
    path('logout/', views.handle_logout),
    path('signup/', views.signup),
    path('items/',views.Item),
    path('items/create-new-category/',views.CreateNewCategory),
    path('items/create-new-item/', views.CreateNewItem),
 
]
