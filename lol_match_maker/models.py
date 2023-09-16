from django.db import models

# Create your models here.


class Champion(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    type = models.CharField(max_length=120)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Lane(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=120, null=False, blank=False)
    main_position = models.CharField(max_length=50)
    main_champion = models.CharField(max_length=50)
    elo = models.CharField(max_length=50)
    champions = models.ManyToManyField(Champion)

    def __str__(self):
        return self.nickname


class Team(models.Model):
    nome = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.nome


class Match(models.Model):
    blue_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='players_blue_team')
    red_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                 related_name='players_red_team')
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f"Partida em {self.created_at} - Azul: {self.blue_team}, Vermelho: {self.red_team}"
