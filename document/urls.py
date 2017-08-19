from django.conf.urls import url

from document import views

urlpatterns = [
    url('^$', views.HomeTemplateView.as_view(), name="home"),
    url('^article/create/$', views.ArticleCreateView.as_view(), name="article_create"),
    url('^article/update/(?P<pk>[\d]+)/$', views.ArticleUpdateView.as_view(), name="article_update"),
    url('^article/detail/(?P<pk>[\d]+)/$', views.ArticleDetailView.as_view(), name="article_detail"),
    url('^category/create/$', views.CategoryCreateView.as_view(), name="category_create"),
]
