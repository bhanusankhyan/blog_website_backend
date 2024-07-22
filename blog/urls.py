from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insert_blog", views.insertBlog, name="insert_blog"),
    path("get_blogs", views.getBlogs, name = "get_blogs"),
    path("get_blog", views.getBlog, name= "get_blog"),
    path('post_comment', views.postComment, name="post_comment"),
    path('login', views.login, name="login"),
    path('sign_up', views.signUp, name="signUp"),
    path('blogs_tag', views.blogsTag, name="blogs_tag"),
    path('delete_blog', views.deleteBlog, name="delete_blog"),
    path('delete_comment', views.deleteComment, name="delete_comment"),
    path('forgot_password', views.forgotPassword, name="forgot_password"),
]
