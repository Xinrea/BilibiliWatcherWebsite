from django.shortcuts import render,redirect
from django.http import HttpResponse
from watch.models import Cards,Upinfo,Accounts,Watch
from django.db.models import Count
from django.contrib.auth.hashers import make_password, check_password

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
    register = False
    if request.method == 'GET':
        v = request.session.get('name')
        if v:
            usern = v
            return render(request,'watch/login.html',{'usern':usern,'register':register})
        else:
            return render(request,'watch/login.html',{'register':register})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        account = Accounts.objects.filter(uname=username).first()
        if check_password(password,account.passwd):
            request.session['name']=account.uname
            request.session['uid']=account.uid
            return redirect('/watch/')
        else:
            return render(request,'watch/login.html',{'error':True,'register':register})

def register(request):
    register = True
    if request.method == 'GET':
        v = request.session.get('name')
        if v:
            usern = v
            return render(request,'watch/login.html',{'usern':usern,'register':register})
        else:
            return render(request,'watch/login.html',{'register':register})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        new_account = Accounts(uname=username,passwd=make_password(password, None, 'pbkdf2_sha256'))
        new_account.save()
        request.session['name']=new_account.uname
        request.session['uid']=new_account.uid
        return redirect('/watch/')

def manage(request,username):
    if request.method == 'GET':
        v = request.session.get('name')
        usrid = request.session.get('uid')
        user = Accounts.objects.filter(uid=usrid).first()
        follow_list = Watch.objects.filter(uid=usrid)
        cardlist = Cards.objects.all()
        uplist = []
        for i in follow_list:
            uplist.append(i.upid)
        if v:
            usern = v
            return render(request,'watch/manage.html',{'usern':usern,'usrid':usrid,'follow':follow_list,'cards':cardlist,'uplist':uplist})
        else :
            return redirect('/watch/login')
    if request.method == 'POST':
        target = request.POST.get('upid')
        new_up = Upinfo.objects.filter(upid=target).first()
        if new_up == None:
            new_up = Upinfo(upid=target)
            new_up.save()
        usrid = request.session.get('uid')
        usrname = request.session.get('name')
        user = Accounts.objects.filter(uid=usrid).first()
        new_watch = Watch(uid=user,upid=new_up)
        new_watch.save()
        return redirect('/watch/user/'+usrname)

def logout(request):
    del request.session['name']
    return redirect('/watch/login')

def delete(request,id):
    v = request.session.get('name')
    usrid = request.session.get('uid')
    delete_obj = Watch.objects.filter(uid=usrid,upid=id)
    if delete_obj:
        delete_obj.delete()
    return redirect('/watch/user/'+v)