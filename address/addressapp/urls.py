from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('useradd/<int:user_id>/', views.useradd, name='useradd'),
    path('update/<int:user_id>/<int:contact_id>/', views.update, name='update'),
    path('delete/<int:user_id>/<int:contact_id>/', views.delete, name='delete'),
]