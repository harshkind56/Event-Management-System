from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import (
    AdminEventListView,
    AddNewEventCreateView,
    AdminEventUpdateView,
    AdminEventDeleteView,
    HomeEventListView,
    
    HomeEventDetailView,
    
    
    
    
   
)

urlpatterns = [
    path('admin_home/', AdminEventListView.as_view(), name='event-index'),
    path('new/', AddNewEventCreateView.as_view(), name='event-create'),
    path('<int:pk>/participant/', views.participants, name='event-participant'),
    path('<int:pk>/update/', AdminEventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/eventdetail/', HomeEventDetailView.as_view(), name='post-detail'),
    path('', HomeEventListView.as_view(), name='event-home'),
    path('home/<int:pk>/register/',views.register, name='event-home-register'),
    path('signup/',views.SignUp, name='signup'),
    path('login/',views.LogIn, name='login'),
    
    path('<int:pk>/delete/', AdminEventDeleteView.as_view(), name='event-delete'),
    path('', HomeEventListView.as_view(), name='event-home'),
    
    
    
   

]