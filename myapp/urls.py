
from django.urls import path
from .views import home, new_post, detail, post_update, post_delete, like

urlpatterns = [
    path('', home, name="home"),
    path("new_post", new_post, name="new_post"),
    path("detail/<str:slug>", detail, name="detail"),    
    path("update/<str:slug>", post_update, name="post_update"),
    path("delete/<str:slug>", post_delete, name="post_delete"),
    path("like/<str:slug>", like, name="like"),  
]