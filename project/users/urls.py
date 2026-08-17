from django.urls import path
from .views import log_in, sign_up, verify_code, user_page, log_out, user_profile, new_post

urlpatterns = [
    path('login/', log_in, name='log_in'),
    path('sign up/', sign_up, name='sign_up'),
    path('verify code/', verify_code, name='verify_code'),
    path('', user_page, name='user_page'),
    path('log_out/', log_out, name='log_out'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('new_post/', new_post, name='new_post')
]
