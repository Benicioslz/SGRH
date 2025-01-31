from django.urls import path
from . import views


urlpatterns = [
    path('tipo_contato_pessoas/list/', views.TipoContatoPessoaListView.as_view(), name='tipo_contato_pessoa_list'),
    path('tipo_contato_pessoas/create/', views.TipoContatoPessoaCreateView.as_view(), name='tipo_contato_pessoa_create'),
    path('tipo_contato_pessoas/<int:pk>/detail/', views.TipoContatoPessoaDetailView.as_view(), name='tipo_contato_pessoa_detail'),
    path('tipo_contato_pessoas/<int:pk>/update/', views.TipoContatoPessoaUpdateView.as_view(), name='tipo_contato_pessoa_update'),
    path('tipo_contato_pessoas/<int:pk>/delete/', views.TipoContatoPessoaDeleteView.as_view(), name='tipo_contato_pessoa_delete'),
]
