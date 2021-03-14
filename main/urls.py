from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('link/', views.Link.as_view(), name='link'),
    path('about/', views.about, name='about')
]
