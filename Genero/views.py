from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class GeneroListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Genero
    template_name = 'genero_list.html'
    context_object_name = 'generos'
    paginate_by = 10
    permission_required = 'generos.view_genero'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class GeneroCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Genero
    template_name = 'genero_create.html'
    form_class = forms.GeneroForm
    success_url = reverse_lazy('genero_list')
    permission_required = 'generos.add_genero'


class GeneroDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Genero
    template_name = 'genero_detail.html'
    permission_required = 'generos.view_genero'


class GeneroUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Genero
    template_name = 'genero_update.html'
    form_class = forms.GeneroForm
    success_url = reverse_lazy('genero_list')
    permission_required = 'generos.change_genero'


class GeneroDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Genero
    template_name = 'genero_delete.html'
    success_url = reverse_lazy('genero_list')
    permission_required = 'generos.delete_genero'
