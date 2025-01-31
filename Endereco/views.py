from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Pessoa.models import Pessoa
from Bairro.models import Bairro
from . import models, forms


class EnderecoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Endereco
    template_name = 'endereco_list.html'
    context_object_name = 'enderecos'
    paginate_by = 10
    permission_required = 'enderecos.view_endereco'

    def get_queryset(self):
        queryset = super().get_queryset()
        logradouro = self.request.GET.get('logradouro')
        cep = self.request.GET.get('cep')
        numero = self.request.GET.get('numero')
        complemento = self.request.GET.get('complemento')
        pessoa = self.request.GET.get('pessoa')
        bairro = self.request.GET.get('bairro')

        if logradouro:
            queryset = queryset.filter(logradouro__icontains=logradouro)
        if cep:
            queryset = queryset.filter(cep__icontains=cep)
        if numero:
            queryset = queryset.filter(numero__icontains=numero)
        if complemento:
            queryset = queryset.filter(complemento__icontains=complemento)
        if pessoa:
            queryset = queryset.filter(pessoa=pessoa)
        if bairro:
            queryset = queryset.filter(bairro=bairro)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pessoas'] = Pessoa.objects.all()
        context['bairros'] = Bairro.objects.all()
        return context


class EnderecoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Endereco
    template_name = 'endereco_create.html'
    form_class = forms.EnderecoForm
    success_url = reverse_lazy('endereco_list')
    permission_required = 'enderecos.add_endereco'


class EnderecoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Endereco
    template_name = 'endereco_detail.html'
    permission_required = 'enderecos.view_endereco'


class EnderecoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Endereco
    template_name = 'endereco_update.html'
    form_class = forms.EnderecoForm
    success_url = reverse_lazy('endereco_list')
    permission_required = 'enderecos.change_endereco'


class EnderecoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Endereco
    template_name = 'endereco_delete.html'
    success_url = reverse_lazy('endereco_list')
    permission_required = 'enderecos.delete_endereco'
