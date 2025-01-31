from django.urls import path
from . import views


urlpatterns = [
    path('pessoas/list/', views.PessoaListView.as_view(), name='pessoa_list'),
    path('pessoas/create/', views.PessoaCreateView.as_view(), name='pessoa_create'),
    path('pessoas/<int:pk>/detail/', views.PessoaDetailView.as_view(), name='pessoa_detail'),
    path('pessoas/<int:pk>/update/', views.PessoaUpdateView.as_view(), name='pessoa_update'),
    path('pessoas/<int:pk>/delete/', views.PessoaDeleteView.as_view(), name='pessoa_delete'),
]
