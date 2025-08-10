from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.main, name="main"),
   path('blog_list/', views.blog_list, name="blog_list"),
  
  path('members/main-blog/<int:pk>/', views.main_blog, name='main_blog'),  # ✅ FIXED
  path('search_blogs/', views.search_blogs, name="search_blogs"),
 ]
 