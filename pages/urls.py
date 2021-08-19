from django.urls import path
from .views import HomePageView, AboutPageView, StatsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('stats/', StatsPageView.as_view(), name='stats'),
]