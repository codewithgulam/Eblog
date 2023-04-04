from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.feed, name='home' ),
    path("create/", login_required(views.addPost) ,name="cr"),
    path("update/<int:id>", login_required(views.upPost) ,name="up"),
    path('post/<int:id>', views.post , name='viewblog'),
    path('register/', views.register , name='register'),

    path('adhome/', login_required(views.adminFeed) , name='admin'),
    path("login/", views.admin_login ,name="in"),
    path("logout/", views.admin_logout ,name="out"),

]
