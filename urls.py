from django.contrib import admin
from django.urls import path, include
from enviroment.views import *
from users_app import urls as users_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enviroment', enviroment_view, name='enviroment'),
    path('', include(users_app_urls)),
]
