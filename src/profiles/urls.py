from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.SocUserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.SocUserPublicView.as_view({'get': 'retrieve'})),
]