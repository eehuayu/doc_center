from django.views import generic

from document import models


class CreateViewWithCategory(generic.CreateView):
    def get_context_data(self, **kwargs):
        ctx = super(CreateViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx


class ListViewWithCategory(generic.ListView):
    def get_context_data(self, **kwargs):
        ctx = super(ListViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx


class TemplateViewWithCategory(generic.TemplateView):
    def get_context_data(self, **kwargs):
        ctx = super(TemplateViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx


class UpdateViewWithCategory(generic.UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super(UpdateViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx


class DetailViewWithCategory(generic.DetailView):
    def get_context_data(self, **kwargs):
        ctx = super(DetailViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx


class DeleteViewWithCategory(generic.DeleteView):
    def get_context_data(self, **kwargs):
        ctx = super(DeleteViewWithCategory, self).get_context_data(**kwargs)

        ctx['category_list'] = models.Category.objects.all()

        return ctx
