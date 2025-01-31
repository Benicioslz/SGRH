from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Pessoa.models import Pessoa
from . import models, forms


class HistoricoSalarialListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.HistoricoSalarial
    template_name = 'historico_salarial_list.html'
    context_object_name = 'historicos_salariais'
    paginate_by = 10
    permission_required = 'historicos_salariais.view_historico_salarial'

    def get_queryset(self):
        queryset = super().get_queryset()
        pessoa = self.request.GET.get('pessoa')
        carga_horaria = self.request.GET.get('carga_horaria')
        salario = self.request.GET.get('salario')
        data_cadastro = self.request.GET.get('data_cadastro')

        if pessoa:
            queryset = queryset.filter(pessoa=pessoa)
        if carga_horaria:
            queryset = queryset.filter(carga_horaria__icontains=carga_horaria)
        if salario:
            queryset = queryset.filter(salario__icontains=salario)
        if data_cadastro:
            queryset = queryset.filter(data_cadastro__icontains=data_cadastro)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pessoas'] = Pessoa.objects.all()
        return context


class HistoricoSalarialCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.HistoricoSalarial
    template_name = 'historico_salarial_create.html'
    form_class = forms.HistoricoSalarialForm
    success_url = reverse_lazy('historico_salarial_list')
    permission_required = 'historicos_salariais.add_historico_salarial'


class HistoricoSalarialDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.HistoricoSalarial
    template_name = 'historico_salarial_detail.html'
    permission_required = 'historicos_salariais.view_historico_salarial'


class HistoricoSalarialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.HistoricoSalarial
    template_name = 'historico_salarial_update.html'
    form_class = forms.HistoricoSalarialForm
    success_url = reverse_lazy('historico_salarial_list')
    permission_required = 'historicos_salariais.change_historico_salarial'


class HistoricoSalarialDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.HistoricoSalarial
    template_name = 'historico_salarial_delete.html'
    success_url = reverse_lazy('historico_salarial_list')
    permission_required = 'historicos_salariais.delete_historico_salarial'
