from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Genero.models import Genero
from . import models, forms


class PessoaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Pessoa
    template_name = 'pessoa_list.html'
    context_object_name = 'pessoas'
    paginate_by = 10
    permission_required = 'pessoas.view_pessoa'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        rg = self.request.GET.get('rg')
        cpf = self.request.GET.get('cpf')
        ctps = self.request.GET.get('ctps')
        data_nascimento = self.request.GET.get('data_nascimento')
        genero = self.request.GET.get('genero')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if rg:
            queryset = queryset.filter(rg__icontains=rg)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)
        if ctps:
            queryset = queryset.filter(ctps__icontains=ctps)
        if data_nascimento:
            queryset = queryset.filter(data_nascimento=data_nascimento)
        if genero:
            queryset = queryset.filter(genero=genero)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context


class PessoaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Pessoa
    template_name = 'pessoa_create.html'
    form_class = forms.PessoaForm
    success_url = reverse_lazy('pessoa_list')
    permission_required = 'pessoas.add_pessoa'


class PessoaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Pessoa
    template_name = 'pessoa_detail.html'
    permission_required = 'pessoas.view_pessoa'


class PessoaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Pessoa
    template_name = 'pessoa_update.html'
    form_class = forms.PessoaForm
    success_url = reverse_lazy('pessoa_list')
    permission_required = 'pessoas.change_pessoa'


class PessoaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Pessoa
    template_name = 'pessoa_delete.html'
    success_url = reverse_lazy('pessoa_list')
    permission_required = 'pessoas.delete_pessoa'
