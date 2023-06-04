from django.urls import path
from . import views, views_api

app_name = 'user_management'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('clients/<int:pk>/', views_api.ClientDetailAPIView.as_view(), name='client-detail'),
]
