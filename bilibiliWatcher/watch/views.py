from django.shortcuts import render,redirect
from django.http import HttpResponse
from watch.models import Cards,Upinfo,Accounts
from django.db.models import Count

# Create your views here.
def index(request):
    upinfos = Upinfo.objects.all()
    cards = Cards.objects.all()
    tag = False
    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/home.html',{'upinfos':upinfos,'cards':cards,'tag':tag,'usern':usern})
    else:
        return render(request,'watch/home.html',{'upinfos':upinfos,'cards':cards,'tag':tag})

def dynamic(request,id):
    up = Upinfo.objects.get(upid=int(id))
    cards = Cards.objects.filter(upid=int(id)).order_by("-ptime")
    type = 0
    tag = False
    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type,'usern':usern})
    else:
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})

    

def dynamic_all(request):
    cards = Cards.objects.order_by("-ptime")
    up = {}
    type = 1
    tag = False
    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type,'usern':usern})
    else:
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})
    

def dynamic_video(request):
    cards = Cards.objects.all()
    up = {}
    type = 2
    tag = False
    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type,'usern':usern})
    else:
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})
    

def dynamic_text(request):
    cards = Cards.objects.all()
    up = {}
    type = 3
    tag = False
    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type,'usern':usern})
    else:
        return render(request,'watch/dynamic.html',{'up':up,'cards':cards,'tag':tag,'type':type})
    

def statistic(request):
    ups = Upinfo.objects.all()
    upnames = []
    data = []
    for i in ups:
        upnames.append(i.upname)
        data.append(Cards.objects.filter(upid=i.upid).aggregate(Count('cardid'))['cardid__count'])

    v = request.session.get('name')
    if v:
        usern = v
        return render(request,'watch/statistic.html',{'upnames':upnames,'data':data,'usern':usern})
    else:
        return render(request,'watch/statistic.html',{'upnames':upnames,'data':data})
    

def login(request):
    if request.method == 'GET':
        v = request.session.get('name')
        if v:
            usern = v
            return render(request,'watch/login.html',{'usern':usern})
        else:
            return render(request,'watch/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        account = Accounts.objects.filter(uname=username,passwd=password).first()
        if account:
            request.session['name']=account.uname
            return redirect('/watch/')
        else:
            return render(request,'watch/login.html',{'error':True})

def manage(request,username):
    return render(request,'watch/manage.html')