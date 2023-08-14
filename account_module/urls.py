from django.urls import path
from .views import RegisterView, ActivatorAccountView, LoginView, LogoutView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('accounts/register/', view=RegisterView.as_view(), name='register-page'),
    path('accounts/active-account/<activator_code>', view=ActivatorAccountView.as_view(), name='active-account-page'),
    path('accounts/reset-password/<activator_code>', view=ResetPasswordView.as_view(), name='reset-password-page'),
    path('accounts/login/', view=LoginView.as_view(), name='login-page'),
    path('accounts/logout/', view=LogoutView.as_view(), name='logout-page'),
    path('accounts/forget-password/', view=ForgotPasswordView.as_view(), name='forget-password-page'),
]
