from . import views
from django.urls import path

urlpatterns = [
    path("index", views.index , name="index"),
    path("ticket", views.ticket , name="ticket"),
    path("portfolio", views.portfolio , name="portfolio"),
    path("gallery/<slug:slug>/", views.gallery , name="gallery"),
    path("video/<slug:slug>/", views.video , name="video"),
   

] 