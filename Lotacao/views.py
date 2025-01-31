from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Pessoa.models import Pessoa
from Setor.models import Setor
from Cargo.models import Cargo
from . import models, forms


class LotacaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Lotacao
    template_name = 'lotacao_list.html'
    context_object_name = 'lotacoes'
    paginate_by = 10
    permission_required = 'lotacoes.view_lotacao'

    def get_queryset(self):
        queryset = super().get_queryset()
        pessoa = self.request.GET.get('pessoa')
        setor = self.request.GET.get('setor')
        cargo = self.request.GET.get('cargo')
        matricula = self.request.GET.get('matricula')
        data_admissao = self.request.GET.get('data_admissao')
        data_demissional = self.request.GET.get('data_demissional')

        if pessoa:
            queryset = queryset.filter(pessoa=pessoa)
        if setor:
            queryset = queryset.filter(setor=setor)
        if cargo:
            queryset = queryset.filter(cargo=cargo)
        if matricula:
            queryset = queryset.filter(matricula__icontains=matricula)
        if data_admissao:
            queryset = queryset.filter(data_admissao=data_admissao)
        if data_demissional:
            queryset = queryset.filter(data_demissional=data_demissional)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pessoas'] = Pessoa.objects.all()
        context['setores'] = Setor.objects.all()
        context['cargos'] = Cargo.objects.all()
        return context


class LotacaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Lotacao
    template_name = 'lotacao_create.html'
    form_class = forms.LotacaoForm
    success_url = reverse_lazy('lotacao_list')
    permission_required = 'lotacoes.add_lotacao'


class LotacaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Lotacao
    template_name = 'lotacao_detail.html'
    permission_required = 'lotacoes.view_lotacao'


class LotacaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Lotacao
    template_name = 'lotacao_update.html'
    form_class = forms.LotacaoForm
    success_url = reverse_lazy('lotacao_list')
    permission_required = 'lotacoes.change_lotacao'


class LotacaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Lotacao
    template_name = 'lotacao_delete.html'
    success_url = reverse_lazy('lotacao_list')
    permission_required = 'lotacoes.delete_lotacao'
