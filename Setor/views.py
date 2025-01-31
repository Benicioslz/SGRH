from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class SetorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Setor
    template_name = 'setor_list.html'
    context_object_name = 'setores'
    paginate_by = 10
    permission_required = 'setores.view_setor'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class SetorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Setor
    template_name = 'setor_create.html'
    form_class = forms.SetorForm
    success_url = reverse_lazy('setor_list')
    permission_required = 'setores.add_setor'


class SetorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Setor
    template_name = 'setor_detail.html'
    permission_required = 'setores.view_setor'


class SetorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Setor
    template_name = 'setor_update.html'
    form_class = forms.SetorForm
    success_url = reverse_lazy('setor_list')
    permission_required = 'setores.change_setor'


class SetorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Setor
    template_name = 'setor_delete.html'
    success_url = reverse_lazy('setor_list')
    permission_required = 'setores.delete_setor'
