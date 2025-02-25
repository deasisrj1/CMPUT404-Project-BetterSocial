from django.urls import path

from . import views

app_name = 'bettersocial'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
]
