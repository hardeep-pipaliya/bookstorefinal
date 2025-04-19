from django.urls import path
from books import views

urlpatterns = [
    path('', views.index, name='book_index'),
    path('book/<int:id>/', views.show, name='show'),
    path('book/<int:id>review/', views.review, name='review'),
    
]
