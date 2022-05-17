
from django.urls import path
from .views import home, new_post, detail

urlpatterns = [
    path('', home, name="home"),
    path("new_post", new_post, name="new_post"),
    path("post/<int:id>", detail, name="detail"),    
]