from django.urls import path
from . import views


urlpatterns = [
    path('tipo_contatos/list/', views.TipoContatoListView.as_view(), name='tipo_contato_list'),
    path('tipo_contatos/create/', views.TipoContatoCreateView.as_view(), name='tipo_contato_create'),
    path('tipo_contatos/<int:pk>/detail/', views.TipoContatoDetailView.as_view(), name='tipo_contato_detail'),
    path('tipo_contatos/<int:pk>/update/', views.TipoContatoUpdateView.as_view(), name='tipo_contato_update'),
    path('tipo_contatos/<int:pk>/delete/', views.TipoContatoDeleteView.as_view(), name='tipo_contato_delete'),
]
