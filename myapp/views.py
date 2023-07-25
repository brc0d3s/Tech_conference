from django.shortcuts import render


rooms=[
    {'id':1,'name':'Let\'s learn Python!',},
    {'id':2,'name':'Design with me',},
    {'id':3,'name':'Frontend developers',},
]

def home(request):
    context={'rooms':rooms}
    return render(request,'myapp/home.html',context)



def room(request,pk):
    room=None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context=context={'room':room}
        
    return render(request,'myapp/room.html',context)

