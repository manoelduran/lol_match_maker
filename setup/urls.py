from django.contrib import admin
from django.urls import path
from lol_match_maker.views import ChampionListView, ChampionCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ChampionListView.as_view(), name="champion_list"),
    path("create", ChampionCreateView.as_view(), name="champion_form"),
]
