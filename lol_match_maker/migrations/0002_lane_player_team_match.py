# Generated by Django 4.2.5 on 2023-09-16 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lol_match_maker", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lane",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=120)),
                ("main_position", models.CharField(max_length=50)),
                ("main_champion", models.CharField(max_length=50)),
                ("elo", models.CharField(max_length=50)),
                ("champions", models.ManyToManyField(
                    to="lol_match_maker.champion")),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("players", models.ManyToManyField(to="lol_match_maker.player")),
            ],
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "blue_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players_blue_team",
                        to="lol_match_maker.team",
                    ),
                ),
                (
                    "red_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players_red_team",
                        to="lol_match_maker.team",
                    ),
                ),
            ],
        ),
    ]
