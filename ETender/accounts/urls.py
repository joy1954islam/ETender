from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,
)


urlpatterns = [
    path('home/', views.home, name='home'),
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),

    path('activate/<code>/', ActivateView.as_view(), name='activate'),

    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    path('holder/change/profile/', views.holder_profile, name='change_profile'),
    path('holder/change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('holder/change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('holder/change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]
