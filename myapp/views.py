from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Let\'s learn Python!', },
#     {'id': 2, 'name': 'Design with me', },
#     {'id': 3, 'name': 'Frontend developers', },
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'myapp/home.html', context)


def room(request, pk):
    room =Room.objects.get(id=pk)
    context = context = {'room': room}

    return render(request, 'myapp/room.html', context)

def createRoom(request):
    context={}
    return render(request,'myapp/room_form.html',context)
