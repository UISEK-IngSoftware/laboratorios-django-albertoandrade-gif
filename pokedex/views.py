from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm


def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})


def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form, 'title': 'Agregar Pokemon'})


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


def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == 'POST':
        pokemon.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'object': pokemon, 'type': 'Pokemon'})


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})


def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})


def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()

    return render(request, 'trainer_form.html', {'form': form, 'title': 'Agregar Entrenador'})


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


def trainer_delete(request, id):
    trainer = get_object_or_404(Trainer, id=id)

    if request.method == 'POST':
        trainer.delete()
        return redirect('trainer_list')

    return render(request, 'confirm_delete.html', {'object': trainer, 'type': 'Entrenador'})