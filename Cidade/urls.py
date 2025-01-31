from django.urls import path
from . import views


urlpatterns = [
    path('cidades/list/', views.CidadeListView.as_view(), name='cidade_list'),
    path('cidades/create/', views.CidadeCreateView.as_view(), name='cidade_create'),
    path('cidades/<int:pk>/detail/', views.CidadeDetailView.as_view(), name='cidade_detail'),
    path('cidades/<int:pk>/update/', views.CidadeUpdateView.as_view(), name='cidade_update'),
    path('cidades/<int:pk>/delete/', views.CidadeDeleteView.as_view(), name='cidade_delete'),
]
