from django.conf.urls import url

from app2.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]