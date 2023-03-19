from django.urls import path
from useraccount.views import SignupView,userlogin,userlogout,profileview,profileupdate

app_name = 'useraccount'
urlpatterns = [
    path('sign-up/',SignupView.as_view(),name='usersignup'),
    path('login/',userlogin,name='userlogin'),
    path('logout/',userlogout,name='userlogout'),
    path('profile/<str:username>/',profileview,name='profileview'),
    path('edit-profile/',profileupdate,name='profileupdate'),
]