from django.urls import path
from .views import homePage,ContactApiView

urlpatterns = [
    path('',homePage,name='home-page'),
    path('contact/',ContactApiView.as_view(),name='contact')
]