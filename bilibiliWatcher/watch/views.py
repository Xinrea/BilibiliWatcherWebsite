from django.shortcuts import render
from django.http import HttpResponse
from watch.models import Cards,Upinfo

# Create your views here.
def index(request):
    upinfos = Upinfo.objects.all()
    cards = Cards.objects.all()
    tag = True
    return render(request,'watch/home.html',{'upinfos':upinfos,'cards':cards,'tag':tag})

def dynamic(request,id):
    up = Upinfo.objects.get(upid=int(id))
    cards = Cards.objects.filter(upid=int(id))
    tag = False
    return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag})