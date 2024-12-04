from django.urls import path
from cars import views

app_name = 'cars'
urlpatterns = [
    path('list/', views.car_list, name='list'),
    path('add/', views.car_add, name='add'),
]