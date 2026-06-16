from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from .forms import PokemonForm, TrainerForm
from .models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer
from .permissions import ReadOnlyOrOAuth2WriteScope


class CustomLoginView(LoginView):
    template_name = 'login_form.html'


def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})


@login_required
def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form, 'title': 'Agregar Pokemon'})


@login_required
def pokemon_edit(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon_detail', id=pokemon.id)
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, 'pokemon_form.html', {'form': form, 'title': 'Editar Pokemon'})


@login_required
def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == 'POST':
        pokemon.delete()
        return redirect('index')

    return render(
        request,
        'confirm_delete.html',
        {'object': pokemon, 'type': 'Pokemon', 'cancel_url': 'index'}
    )


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})


def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})


@login_required
def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()

    return render(request, 'trainer_form.html', {'form': form, 'title': 'Agregar Entrenador'})


@login_required
def trainer_edit(request, id):
    trainer = get_object_or_404(Trainer, id=id)

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', id=trainer.id)
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'trainer_form.html', {'form': form, 'title': 'Editar Entrenador'})


@login_required
def trainer_delete(request, id):
    trainer = get_object_or_404(Trainer, id=id)

    if request.method == 'POST':
        trainer.delete()
        return redirect('trainer_list')

    return render(
        request,
        'confirm_delete.html',
        {'object': trainer, 'type': 'Entrenador', 'cancel_url': 'trainer_list'}
    )


@require_POST
def logout_user(request):
    logout(request)
    return redirect('index')



class TrainerViewSet(viewsets.ModelViewSet):
    """API REST para listar, crear, consultar, actualizar y eliminar entrenadores."""

    queryset = Trainer.objects.all().order_by('id')
    serializer_class = TrainerSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [ReadOnlyOrOAuth2WriteScope]


class PokemonViewSet(viewsets.ModelViewSet):
    """API REST para listar, crear, consultar, actualizar y eliminar pokemons."""

    queryset = Pokemon.objects.all().order_by('id')
    serializer_class = PokemonSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [ReadOnlyOrOAuth2WriteScope]
