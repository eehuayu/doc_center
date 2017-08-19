from django.conf.urls import url

from document import views

urlpatterns = [
    url('^$', views.HomeTemplateView.as_view(), name="home"),
    url('^article/create/$', views.ArticleCreateView.as_view(), name="article_create"),
    url('^article/update/(?P<pk>[\d]+)/$', views.ArticleUpdateView.as_view(), name="article_update"),
    url('^article/detail/(?P<pk>[\d]+)/$', views.ArticleDetailView.as_view(), name="article_detail"),
    url('^category/create/$', views.CategoryCreateView.as_view(), name="category_create"),
    url('^upload/$', views.UploadCreateView.as_view(), name="upload"),
    url('^upload/list/$', views.UploadListView.as_view(), name="upload_list"),
    url('^delete/file/$', views.FileDeleteView.as_view(), name="delete_file"),
]
