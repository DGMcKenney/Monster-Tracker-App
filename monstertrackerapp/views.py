from django.shortcuts import render, get_object_or_404
from .models import Monster, Sighting
from .forms import MonsterForm, SightingForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'monstertrackerapp/index.html')

def get_monsters(request):
    monster_list = Monster.objects.all()
    return render(request, 'monstertrackerapp/monsters.html', {'monster_list': monster_list})

def monster_details(request, id):
    monster_deets = get_object_or_404(Monster, pk=id)
    return render(request, 'monstertrackerapp/monster_details.html', {'monster_deets': monster_deets})

def get_sightings(request):
    sighting_list = Sighting.objects.all()
    return render(request, 'monstertrackerapp/sightings.html', {'sighting_list': sighting_list})

def sighting_details(request, id):
    sighting_deets = get_object_or_404(Sighting, pk=id)
    return render(request, 'monstertrackerapp/sighting_details.html', {'sighting_deets': sighting_deets})

@login_required
def new_monster(request):
    form = MonsterForm
    if request.method == 'POST':
        form = MonsterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MonsterForm()
    else:
        form = MonsterForm()
    return render(request, 'monstertrackerapp/new_monster.html', {'form': form})

@login_required
def new_sighting(request):
    form = SightingForm
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = SightingForm()
    else:
        form = SightingForm()
    return render(request, 'monstertrackerapp/new_sighting.html', {'form': form})

def loginmessage(request):
    return render(request, 'monstertrackerapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'monstertrackerapp/logoutmessage.html')