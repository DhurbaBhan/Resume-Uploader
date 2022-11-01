from django.urls import path
from . import views

urlpatterns = [

  path('',views.register,name='register'),
  path('login/',views.user_login,name='login'),
  path('logout/',views.logout,name='logout'),
  path('dashboard/',views.HomeView.as_view(),name='home'),
  path('user/<int:idd>',views.user,name='user'),
]
