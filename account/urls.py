from django.urls import path

from .views import logout_page, login_page, register_page

urlpatterns = [
    path('logout', logout_page, name='logout'),
    path('login', login_page, name='login'),
    path('register', register_page, name='register'),
]
