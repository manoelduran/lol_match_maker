from django.contrib import admin
from django.urls import path
from lol_match_maker.views import ChampionListView, ChampionCreateView, ChampionUpdateView, ChampionDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ChampionListView.as_view(), name="champion_list"),
    path("create", ChampionCreateView.as_view(), name="champion_form"),
    path('update/<int:pk>/', ChampionUpdateView.as_view(),
         name="champion_form"),
    path('delete/<int:pk>/', ChampionDeleteView.as_view(),
         name="champion_confirm_delete")
]
