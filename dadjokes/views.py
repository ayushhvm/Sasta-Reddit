from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm


# Create your views here.

def home(request):
    q = request.GET.get('q')
    rooms = Room.objects.filter(topic__name=q)
    topics = Topic.objects.all()
    context = { 'rooms':rooms, 'topics':topics }
    return render(request,'dadjokes/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = { 'room':room }        
    return render(request,'dadjokes/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request,'dadjokes/room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request,'dadjokes/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'dadjokes/delete.html' ,{'obj':room})