from django.urls import path
from .views import HomePageView, separate, AboutView
from . import views

urlpatterns = [
    path('main/', HomePageView.as_view(), name='home'),
    path('audio',views.Audio_store, name='audio'),
    path('result/', separate, name='separate'),
    path('', AboutView.as_view(), name='about')
]
