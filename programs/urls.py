from django.urls import path
from programs import views

app_name = 'programs'
urlpatterns = [
    path('list/', views.program_list, name='list'),
    path('add/', views.program_add, name='add'),
]