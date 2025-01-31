from django.urls import path
from . import views


urlpatterns = [
    path('enderecos/list/', views.EnderecoListView.as_view(), name='endereco_list'),
    path('enderecos/create/', views.EnderecoCreateView.as_view(), name='endereco_create'),
    path('enderecos/<int:pk>/detail/', views.EnderecoDetailView.as_view(), name='endereco_detail'),
    path('enderecos/<int:pk>/update/', views.EnderecoUpdateView.as_view(), name='endereco_update'),
    path('enderecos/<int:pk>/delete/', views.EnderecoDeleteView.as_view(), name='endereco_delete'),
]
