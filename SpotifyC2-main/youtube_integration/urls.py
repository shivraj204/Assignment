from django.urls import path
from . import views

app_name = 'youtube'

urlpatterns = [
    path('<int:sid>/', views.index, name='index'),
    path('search/<int:sid>/', views.search, name='search'),
]