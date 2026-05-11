from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='trainers/', null=True, blank=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=50, null=False)
    height = models.FloatField()
    weight = models.FloatField()
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name='pokemons',
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True)

    def __str__(self):
        return self.name