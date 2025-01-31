from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Tipo_Contato.models import TipoContato
from Pessoa.models import Pessoa
from . import models, forms


class TipoContatoPessoaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.TipoContatoPessoa
    template_name = 'tipo_contato_pessoa_list.html'
    context_object_name = 'tipo_contato_pessoas'
    paginate_by = 10
    permission_required = 'tipo_contato_pessoas.view_tipo_contato_pessoa'

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_contato = self.request.GET.get('tipo_contato')
        pessoa = self.request.GET.get('pessoa')
        contato = self.request.GET.get('contato')

        if tipo_contato:
            queryset = queryset.filter(tipo_contato=tipo_contato)
        if pessoa:
            queryset = queryset.filter(pessoa=pessoa)
        if contato:
            queryset = queryset.filter(contato__icontains=contato)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_contatos'] = TipoContato.objects.all()
        context['pessoas'] = Pessoa.objects.all()
        return context


class TipoContatoPessoaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.TipoContatoPessoa
    template_name = 'tipo_contato_pessoa_create.html'
    form_class = forms.TipoContatoPessoaForm
    success_url = reverse_lazy('tipo_contato_pessoa_list')
    permission_required = 'tipo_contato_pessoas.add_tipo_contato_pessoa'


class TipoContatoPessoaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.TipoContatoPessoa
    template_name = 'tipo_contato_pessoa_detail.html'
    permission_required = 'tipo_contato_pessoas.view_tipo_contato_pessoa'


class TipoContatoPessoaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.TipoContatoPessoa
    template_name = 'tipo_contato_pessoa_update.html'
    form_class = forms.TipoContatoPessoaForm
    success_url = reverse_lazy('tipo_contato_pessoa_list')
    permission_required = 'tipo_contato_pessoas.change_tipo_contato_pessoa'


class TipoContatoPessoaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.TipoContatoPessoa
    template_name = 'tipo_contato_pessoa_delete.html'
    success_url = reverse_lazy('tipo_contato_pessoa_list')
    permission_required = 'tipo_contato_pessoas.delete_tipo_contato_pessoa'
