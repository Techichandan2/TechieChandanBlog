from django.urls import path
from blog import views



urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.showAllPost, name='showAllPost'),
    path('posts/post_comment', views.postcomment, name='postcomment'),
    
    path('posts/<str:slug>', views.posts, name='posts'),
    path('posts/category/<str:category>/', views.filterposts, name='filterposts'),
    path('posts/category/<str:slug1>/<str:slug2>', views.posts2, name='posts'),
    path('about/', views.about, name='about'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    
]