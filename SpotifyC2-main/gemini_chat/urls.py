from django.urls import path
from . import views

app_name = 'gemini'

urlpatterns = [
    path('chat/<int:sid>/', views.chat_view, name='chat'),
    path('api/send-message/<int:sid>/', views.send_message, name='send_message'),
]