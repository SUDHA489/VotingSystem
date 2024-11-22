from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('vote/<int:pk1>/<str:pk2>/', views.vote, name='vote'),
    path('results/',views.results,name='results'),
]