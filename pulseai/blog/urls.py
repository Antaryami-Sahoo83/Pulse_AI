from django.urls import path # type: ignore
from blog import views

urlpatterns = [
      path('', views.index, name="home"),
#     path('about/', views.about,name="about"),
#     path('contact/', views.contact,name="contact")
]