from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class EstadoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Estado
    template_name = 'estado_list.html'
    context_object_name = 'estados'
    paginate_by = 10
    permission_required = 'estados.view_estado'

    def get_queryset(self):
        queryset = super().get_queryset()
        sigla = self.request.GET.get('sigla')
        nome = self.request.GET.get('nome')

        if sigla:
            queryset = queryset.filter(sigla__icontains=sigla)
        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class EstadoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Estado
    template_name = 'estado_create.html'
    form_class = forms.EstadoForm
    success_url = reverse_lazy('estado_list')
    permission_required = 'estados.add_estado'


class EstadoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Estado
    template_name = 'estado_detail.html'
    permission_required = 'estados.view_estado'


class EstadoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Estado
    template_name = 'estado_update.html'
    form_class = forms.EstadoForm
    success_url = reverse_lazy('estado_list')
    permission_required = 'estados.change_estado'


class EstadoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Estado
    template_name = 'estado_delete.html'
    success_url = reverse_lazy('estado_list')
    permission_required = 'estados.delete_estado'
