from django.urls import path
from . import views


urlpatterns = [
    path('lotacoes/list/', views.LotacaoListView.as_view(), name='lotacao_list'),
    path('lotacoes/create/', views.LotacaoCreateView.as_view(), name='lotacao_create'),
    path('lotacoes/<int:pk>/detail/', views.LotacaoDetailView.as_view(), name='lotacao_detail'),
    path('lotacoes/<int:pk>/update/', views.LotacaoUpdateView.as_view(), name='lotacao_update'),
    path('lotacoes/<int:pk>/delete/', views.LotacaoDeleteView.as_view(), name='lotacao_delete'),
]
