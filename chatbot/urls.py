# chatbot/urls.py
 

from django.urls import path
from . import views
from .views import chatbot_page, chatbot_view

urlpatterns = [

    path('api/', chatbot_view, name='chatbot_view'),

     
    path('', chatbot_page, name='chatbot_page'),   # Página HTML do chatbot
    path('chatbot/', chatbot_view, name='chatbot'),
    path('chatbot/api/', chatbot_view, name='chatbot_api'), 
    path('', chatbot_page, name='chatbot_page'),  # Página HTML do chatbot
     



]
