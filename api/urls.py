from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.ProfileView.as_view(), name='resume'),
    path('showlist/', views.ProfileView.as_view(), name='resume'),
]
