from django.urls import path

from carworld.common.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
]
