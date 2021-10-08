from django.urls import path
from django.contrib.auth import views as auth_views

from .views import logout_page, login_page, register_page, email_activate, register_subscriber

urlpatterns = [
    path('logout', logout_page, name='logout'),
    path('login', login_page, name='login'),
    path('register', register_page, name='register'),
    path('activate/<str:uidb64>/<str:token>', email_activate, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset-password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
         name='password_reset_complete'),
    path('subscribe/', register_subscriber, name="register_subscriber"),

]
