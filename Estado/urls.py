from django.urls import path
from . import views


urlpatterns = [
    path('estados/list/', views.EstadoListView.as_view(), name='estado_list'),
    path('estados/create/', views.EstadoCreateView.as_view(), name='estado_create'),
    path('estados/<int:pk>/detail/', views.EstadoDetailView.as_view(), name='estado_detail'),
    path('estados/<int:pk>/update/', views.EstadoUpdateView.as_view(), name='estado_update'),
    path('estados/<int:pk>/delete/', views.EstadoDeleteView.as_view(), name='estado_delete'),
]
