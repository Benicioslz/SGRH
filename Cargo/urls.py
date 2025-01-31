from django.urls import path
from . import views


urlpatterns = [
    path('cargos/list/', views.CargoListView.as_view(), name='cargo_list'),
    path('cargos/create/', views.CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/<int:pk>/detail/', views.CargoDetailView.as_view(), name='cargo_detail'),
    path('cargos/<int:pk>/update/', views.CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/<int:pk>/delete/', views.CargoDeleteView.as_view(), name='cargo_delete'),
]
