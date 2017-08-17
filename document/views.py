from django.shortcuts import render

# Create your views here.
from django.views import generic

from document import models


class HomeView(generic.TemplateView):
    template_name = "document/home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        category_list = models.Category.objects.all()
        ctx['data'] = dict()
        for category in category_list:
            ctx['data'][category] = category.articles.all()

        return ctx
