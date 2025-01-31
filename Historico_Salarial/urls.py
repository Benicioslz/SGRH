from django.urls import path
from . import views


urlpatterns = [
    path('historicos_salariais/list/', views.HistoricoSalarialListView.as_view(), name='historico_salarial_list'),
    path('historicos_salariais/create/', views.HistoricoSalarialCreateView.as_view(), name='historico_salarial_create'),
    path('historicos_salariais/<int:pk>/detail/', views.HistoricoSalarialDetailView.as_view(), name='historico_salarial_detail'),
    path('historicos_salariais/<int:pk>/update/', views.HistoricoSalarialUpdateView.as_view(), name='historico_salarial_update'),
    path('historicos_salariais/<int:pk>/delete/', views.HistoricoSalarialDeleteView.as_view(), name='historico_salarial_delete'),
]
