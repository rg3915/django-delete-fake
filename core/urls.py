from django.urls import path

from . import views

urlpatterns = [
    path('', views.PessoaListView.as_view(), name='pessoa-list'),
    path('create/', views.PessoaCreateView.as_view(), name='pessoa-create'),
    path('<int:pk>/', views.PessoaDetailView.as_view(), name='pessoa-detail'),
    path('<int:pk>/delete/', views.PessoaDeleteView.as_view(), name='pessoa-delete'),
    path('<int:pk>/update/', views.PessoaUpdateView.as_view(), name='pessoa-update'),
]
