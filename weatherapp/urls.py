from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('signin/',views.signin_view,name='signin'),
    path('signout/',views.logout_view,name='signout'),
    path('weather/',views.weather,name='weather')
]
