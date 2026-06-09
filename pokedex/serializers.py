from rest_framework import serializers

from .models import Pokemon, Trainer


class TrainerSerializer(serializers.ModelSerializer):
    pokemons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Trainer
        fields = ['id', 'name', 'age', 'city', 'photo', 'pokemons']


class PokemonSerializer(serializers.ModelSerializer):
    trainer_name = serializers.CharField(source='trainer.name', read_only=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name',
            'type',
            'height',
            'weight',
            'trainer',
            'trainer_name',
            'image',
        ]
