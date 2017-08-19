from django.urls import reverse_lazy, reverse

from document import models, mixins


class HomeTemplateView(mixins.TemplateViewWithCategory):
    template_name = "document/home.html"


class ArticleCreateView(mixins.CreateViewWithCategory):
    template_name = "document/write.html"
    model = models.Article
    fields = ("title", "content", "category",)

    def get_success_url(self):
        return reverse('article_detail', kwargs=dict(pk=self.object.id))

    def get_context_data(self, **kwargs):
        ctx = super(ArticleCreateView, self).get_context_data(**kwargs)
        ctx['category_list'] = models.Category.objects.all()
        return ctx


class ArticleUpdateView(mixins.UpdateViewWithCategory):
    template_name = "document/write.html"
    model = models.Article
    fields = ("title", "content", "category",)

    def get_success_url(self):
        return reverse('article_detail', kwargs=dict(pk=self.object.id))

    def get_context_data(self, **kwargs):
        ctx = super(ArticleUpdateView, self).get_context_data(**kwargs)
        ctx['category_list'] = models.Category.objects.all()
        return ctx


class ArticleDetailView(mixins.DetailViewWithCategory):
    template_name = "document/article_detail.html"
    model = models.Article


class CategoryCreateView(mixins.CreateViewWithCategory):
    template_name = "document/category_create.html"
    model = models.Category
    fields = ("name", )
    success_url = reverse_lazy('home')


