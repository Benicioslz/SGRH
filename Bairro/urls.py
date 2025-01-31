from django.urls import path
from . import views


urlpatterns = [
    path('bairros/list/', views.BairroListView.as_view(), name='bairro_list'),
    path('bairros/create/', views.BairroCreateView.as_view(), name='bairro_create'),
    path('bairros/<int:pk>/detail/', views.BairroDetailView.as_view(), name='bairro_detail'),
    path('bairros/<int:pk>/update/', views.BairroUpdateView.as_view(), name='bairro_update'),
    path('bairros/<int:pk>/delete/', views.BairroDeleteView.as_view(), name='bairro_delete'),
]
