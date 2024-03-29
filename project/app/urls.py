from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tech/', views.TechPageView.as_view(), name='tech'),
    path('archive/', views.ArchivePageView.as_view(), name='archive'),
    path("archive/<slug:pk>/", views.PopUpPage.as_view(), name="popup"),
]
