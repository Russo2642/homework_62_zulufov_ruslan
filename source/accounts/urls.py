from accounts.views import LoginView, logout_view, RegisterView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
