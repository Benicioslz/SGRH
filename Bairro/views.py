from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from Cidade.models import Cidade


class BairroListView(ListView):
    model = models.Bairro
    template_name = 'bairro_list.html'
    context_object_name = 'bairros'
    permission_required = 'bairros.view_bairro'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        cidade = self.request.GET.get('cidade')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if cidade:
            queryset = queryset.filter(cidade=cidade)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cidades'] = Cidade.objects.all()
        return context


class BairroCreateView(CreateView):
    model = models.Bairro
    template_name = 'bairro_create.html'
    form_class = forms.BairroForm
    success_url = reverse_lazy('bairro_list')
    permission_required = 'bairros.add_bairro'


class BairroDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Bairro
    template_name = 'bairro_detail.html'
    permission_required = 'bairros.view_bairro'


class BairroUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Bairro
    template_name = 'bairro_update.html'
    form_class = forms.BairroForm
    success_url = reverse_lazy('bairro_list')
    permission_required = 'bairros.change_bairro'


class BairroDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Bairro
    template_name = 'bairro_delete.html'
    success_url = reverse_lazy('bairro_list')
    permission_required = 'bairros.delete_bairro'
