from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from carworld.core.views import BootStrapFormViewMixin
from carworld.others.forms import EditSourceForm
from carworld.others.models import Source


class ListSourcesView(ListView):
    template_name = 'others/other_list.html'
    context_object_name = 'sources'
    model = Source


class CreateSourceView(LoginRequiredMixin, BootStrapFormViewMixin, CreateView):
    model = Source
    fields = ('name', 'image', 'description', 'url')
    success_url = reverse_lazy('list sources')
    template_name = 'others/other_create.html'

    def form_valid(self, form):
        source = form.save(commit=False)
        source.user = self.request.user
        source.save()
        return super().form_valid(form)


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'others/other_detail.html'
    context_object_name = 'source'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source = context['source']

        is_owner = source.user == self.request.user

        context['is_owner'] = is_owner

        return context


class EditSourceView(LoginRequiredMixin, UpdateView):
    model = Source
    template_name = 'others/other_edit.html'
    form_class = EditSourceForm
    success_url = reverse_lazy('list sources')


class DeleteSourceView(LoginRequiredMixin, DeleteView):
    template_name = 'others/other_delete.html'
    model = Source
    success_url = reverse_lazy('list sources')