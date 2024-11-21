from django.urls import path
from django.contrib.auth import views as auth_views  
from .views import ArticleListCreateView, ArticleDetailView
from django.contrib import admin
from . import views
from django.urls import path, include
from chatbot import views as chatbot_views
 

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('chatbot/', chatbot_views.chatbot_view, name='chatbot_view'), 
   #path('chatbot/', views.chatbot_view, name='chatbot_view'),  # URL para a view do chatbot
]