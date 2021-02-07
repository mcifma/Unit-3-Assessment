from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wacky
from .forms import WackyForm


# Create your views here.

def home(request):
    
    form = WackyForm()

    if request.method == 'POST':
        print(request.POST)
        form = WackyForm(request.POST)
        if form_is_valid():
            form.save()
            return redirect('/')
        
    keeys = {'form':form}
    return render(request, 'home.html', keeys)


def createWacky(request):

    form = WackyForm()
    if request.method == 'POST':
        form = WackyForm(request.POST)
        if form.is_valid():
            new_wacky = form.save(commit=False)
            new_wacky.wacky_id = wacky_id
            new_wacky.save()
        return redirect('/', wacky_id=wacky_id)

    context = {'form': form}
    return render(request, 'home.html', context)


def deleteWacky(request, pk):
    wacky = Wacky.objects.get(id=pk)
    if request.method == "POST":
        wacky.delete()
        return redirect('/')

    context = {'item': wacky}
    return render(request, 'home.html', context)

# class WackyCreate(CreateView):
#   model = Widget
#   fields = '__all__'
#   success_url = '/wackys/'

# class WackyDelete(DeleteView):
#   model = Cat
#   success_url = '/wackys/'