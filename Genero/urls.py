from django.urls import path
from . import views


urlpatterns = [
    path('generos/list/', views.GeneroListView.as_view(), name='genero_list'),
    path('generos/create/', views.GeneroCreateView.as_view(), name='genero_create'),
    path('generos/<int:pk>/detail/', views.GeneroDetailView.as_view(), name='genero_detail'),
    path('generos/<int:pk>/update/', views.GeneroUpdateView.as_view(), name='genero_update'),
    path('generos/<int:pk>/delete/', views.GeneroDeleteView.as_view(), name='genero_delete'),
]
