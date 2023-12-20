from django.urls import path,include
from host_website import views

urlpatterns = [
    path('', views.host, name='host' ),
    
]