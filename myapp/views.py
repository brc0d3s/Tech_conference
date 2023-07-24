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
    return render(request,'myapp/room.html')

