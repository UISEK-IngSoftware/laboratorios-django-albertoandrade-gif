from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),

    path('pokemon/<int:id>/', views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/agregar/', views.pokemon_create, name='pokemon_create'),
    path('pokemon/<int:id>/editar/', views.pokemon_edit, name='pokemon_edit'),
    path('pokemon/<int:id>/eliminar/', views.pokemon_delete, name='pokemon_delete'),

    path('entrenadores/', views.trainer_list, name='trainer_list'),
    path('entrenadores/agregar/', views.trainer_create, name='trainer_create'),
    path('entrenadores/<int:id>/', views.trainer_detail, name='trainer_detail'),
    path('entrenadores/<int:id>/editar/', views.trainer_edit, name='trainer_edit'),
    path('entrenadores/<int:id>/eliminar/', views.trainer_delete, name='trainer_delete'),
]
