from django.contrib import admin
from django.urls import path, include
from items.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),

]


