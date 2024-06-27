from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('wait/',views.wait,name='wait'),
    path('superuser/',views.superuser,name='superuser'),
    path('userprofile/',views.userprofile,name='userprofile'),
]
