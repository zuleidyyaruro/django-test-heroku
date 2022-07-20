from django.urls import URLPattern, path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
