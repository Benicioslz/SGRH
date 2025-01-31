from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from Estado.models import Estado


class CidadeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Cidade
    template_name = 'cidade_list.html'
    context_object_name = 'cidades'
    paginate_by = 10
    permission_required = 'cidades.view_cidade'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        estado = self.request.GET.get('estado')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estado.objects.all()
        return context


class CidadeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Cidade
    template_name = 'cidade_create.html'
    form_class = forms.CidadeForm
    success_url = reverse_lazy('cidade_list')
    permission_required = 'cidades.add_cidade'


class CidadeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Cidade
    template_name = 'cidade_detail.html'
    permission_required = 'cidades.view_cidade'


class CidadeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Cidade
    template_name = 'cidade_update.html'
    form_class = forms.CidadeForm
    success_url = reverse_lazy('cidade_list')
    permission_required = 'cidades.change_cidade'


class CidadeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Cidade
    template_name = 'cidade_delete.html'
    success_url = reverse_lazy('cidade_list')
    permission_required = 'cidades.delete_cidade'
