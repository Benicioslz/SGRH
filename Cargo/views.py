from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class CargoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Cargo
    template_name = 'cargo_list.html'
    context_object_name = 'cargos'
    paginate_by = 10
    permission_required = 'cargos.view_cargo'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class CargoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Cargo
    template_name = 'cargo_create.html'
    form_class = forms.CargoForm
    success_url = reverse_lazy('cargo_list')
    permission_required = 'cargos.add_cargo'


class CargoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Cargo
    template_name = 'cargo_detail.html'
    permission_required = 'cargos.view_cargo'


class CargoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Cargo
    template_name = 'cargo_update.html'
    form_class = forms.CargoForm
    success_url = reverse_lazy('cargo_list')
    permission_required = 'cargos.change_cargo'


class CargoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Cargo
    template_name = 'cargo_delete.html'
    success_url = reverse_lazy('cargo_list')
    permission_required = 'cargos.delete_cargo'
