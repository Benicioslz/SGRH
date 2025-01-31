from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class TipoContatoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TipoContato
    template_name = 'tipo_contato_list.html'
    context_object_name = 'tipo_contatos'
    paginate_by = 10
    permission_required = 'tipo_contatos.view_tipo_contato'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class TipoContatoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TipoContato
    template_name = 'tipo_contato_create.html'
    form_class = forms.TipoContatoForm
    success_url = reverse_lazy('tipo_contato_list')
    permission_required = 'tipo_contatos.add_tipo_contato'


class TipoContatoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TipoContato
    template_name = 'tipo_contato_detail.html'
    permission_required = 'tipo_contatos.view_tipo_contato'


class TipoContatoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TipoContato
    template_name = 'tipo_contato_update.html'
    form_class = forms.TipoContatoForm
    success_url = reverse_lazy('tipo_contato_list')
    permission_required = 'tipo_contatos.change_tipo_contato'


class TipoContatoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TipoContato
    template_name = 'tipo_contato_delete.html'
    success_url = reverse_lazy('tipo_contato_list')
    permission_required = 'tipo_contatos.delete_tipo_contato'
