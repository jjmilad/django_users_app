from django.urls import path, include

from .views import *

urlpatterns = [
    path('sign_in', sign_in_page, name='sign_in'),
    path('sign_up', sign_up_page, name='sign_up'),
    path('account', account_page, name='account'),
    path('account/log_out', log_out_user_page, name='user_log_out'),
    path('forgot_password', forgot_password_page, name='forgot_password'),
]
