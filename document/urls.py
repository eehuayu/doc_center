from django.conf.urls import url

from document import views

urlpatterns = [
    url('^$', views.HomeView.as_view(), name="home"),
]
