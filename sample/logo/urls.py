from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('settings/', views.settings_view, name='settings'),
    path('profile/', views.profile_view, name='profile'),
    path('create/', views.person_create, name='person_create'),
    path('update/<int:pk>/', views.person_update, name='person_update'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),
]