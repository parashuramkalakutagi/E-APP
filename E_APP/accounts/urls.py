from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *



accounts = DefaultRouter()

accounts.register('profile',Profile_Register,basename='profile')
accounts.register('Login',LoginViewset,basename='Login')
accounts.register('LogOut',LogOutViewset,basename='LogOut')
accounts.register('ForgotPassword',ForgotPasswordViewset,basename='ForgotPassword')
accounts.register('verifyOtpView',verifyOtpView,basename='verifyOtpView')
accounts.register('NewPassword',NewPassword,basename='NewPassword')

urlpatterns = [
    path('',include(accounts.urls)),
]