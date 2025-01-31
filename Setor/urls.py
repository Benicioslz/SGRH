from django.urls import path
from . import views


urlpatterns = [
    path('setores/list/', views.SetorListView.as_view(), name='setor_list'),
    path('setores/create/', views.SetorCreateView.as_view(), name='setor_create'),
    path('setores/<int:pk>/detail/', views.SetorDetailView.as_view(), name='setor_detail'),
    path('setores/<int:pk>/update/', views.SetorUpdateView.as_view(), name='setor_update'),
    path('setores/<int:pk>/delete/', views.SetorDeleteView.as_view(), name='setor_delete'),
]
