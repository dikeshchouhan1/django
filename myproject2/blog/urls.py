from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:post_id>/',views.post_details,name="post_details"),
    path('user/<str:username>/',views.post_profile,name="user_profile"),
]
