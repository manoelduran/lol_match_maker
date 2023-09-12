from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Champion
from .forms import ChampionForm


class ChampionListView(View):
    def get(self, request):
        champions = Champion.objects.all()
        return render(request, 'lol_match_maker/champion_list.html', {'champion_list': champions})


class ChampionCreateView(View):
    # get template
    def get(self, request):
        form = ChampionForm()
        return render(request, 'lol_match_maker/champion_form.html', {'form': form})
    # Submit

    def post(self, request):
        form = ChampionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            champion = Champion(name=name, type=type)
            champion.save()
            return HttpResponseRedirect(reverse("champion_list"))
        return render(request, 'lol_match_maker/champion_form.html', {'form': form})


"""
class ChampionUpdateView(View):
    def get(self, request, pk):
        champion = get_object_or_404(Champion, pk=pk)
        form = ChampionForm(instance=champion)
        return render(request, 'champion_form.html', {'form': form, 'champion': champion})

    def post(self, request, pk):
        champion = get_object_or_404(Champion, pk=pk)
        form = ChampionForm(request.POST, instance=champion)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('champion-list'))
        return render(request, 'champion_form.html', {'form': form, 'champion': champion})


class ChampionDeleteView(View):
    def get(self, request, pk):
        champion = get_object_or_404(Champion, pk=pk)
        return render(request, 'champion_confirm_delete.html', {'champion': champion})

    def post(self, request, pk):
        champion = get_object_or_404(Champion, pk=pk)
        champion.delete()
        return HttpResponseRedirect(reverse('champion-list'))
  """
