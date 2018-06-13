from django.shortcuts import render
from django.http import HttpResponse
from watch.models import Cards,Upinfo
from django.db.models import Count

# Create your views here.
def index(request):
    upinfos = Upinfo.objects.all()
    cards = Cards.objects.all()
    tag = True
    return render(request,'watch/home.html',{'upinfos':upinfos,'cards':cards,'tag':tag})

def dynamic(request,id):
    up = Upinfo.objects.get(upid=int(id))
    cards = Cards.objects.filter(upid=int(id)).order_by("-ptime")
    type = 0
    tag = False
    return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})

def dynamic_all(request):
    cards = Cards.objects.order_by("-ptime")
    up = {}
    type = 1
    tag = False
    return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})

def dynamic_video(request):
    cards = Cards.objects.all()
    up = {}
    type = 2
    tag = False
    return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})

def dynamic_text(request):
    cards = Cards.objects.all()
    up = {}
    type = 3
    tag = False
    return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})

def statistic(request):
    ups = Upinfo.objects.all()
    upnames = []
    data = []
    for i in ups:
        upnames.append(i.upname)
        data.append(Cards.objects.filter(upid=i.upid).aggregate(Count('cardid'))['cardid__count'])
    return render(request,'watch/statistic.html',{'upnames':upnames,'data':data})

def login(request):
    return render(request,'watch/login.html')