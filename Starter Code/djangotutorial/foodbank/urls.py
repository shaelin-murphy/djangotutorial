from django.urls import path
from . import views

app_name = 'foodbank'

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('intake/', views.client_intake, name='client_intake'),
    path('clients/<int:client_id>/add-visit/', views.add_intake_record, name='add_intake_record'),
]
