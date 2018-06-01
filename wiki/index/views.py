from django.shortcuts import render
from collections import OrderedDict
import pickle
from .models import SomeObject
from django.contrib.auth.decorators import login_required
import re, os, bz2
from sortedcontainers import SortedDict
#import requests
#from bs4 import BeautifulSoup


pickle_off = open("demo.pickle","rb")
index = open("index.txt","rb")
new_dict = pickle.load(pickle_off)
d = {}
for line in index:
    (key, val1, val2) = line.split()
    d[int(val2)] = key
sd = SortedDict((key, value) for key, value in d.items())
doc = '<doc'

# Create your views here.
#@login_required
def index(request):
    global new_dict
    a = []
    c=0
    if request.POST:
        text1 = request.POST.get('text1')
        for n in new_dict.keys():
            if text1.lower() in n.lower():
                a.append(n)
                c=c+1
                if c>20:
                    break
        context = {'keys':a}
    else:
        context = {}
    return render(request, "index.html", context)

#@login_required
def search(request):
    global new_dict
    if 'selection' in request.POST:
        spid = request.POST.get('selection')
        request.session['spid'] = spid
        col = {}
        for c in new_dict[spid]:
            f = 0
            e = 0
            for a in new_dict[spid][c]:
                f = f + 1
                obj = SomeObject()
                obj.args = {spid:{c:{a}}}
                ob = SomeObject.objects.filter(args=obj.args).count()
                e = e + ob
            col[c] = [f, e]
        print(col)
        context = {'col': col}
        return render(request, "search.html", context)
    if 'error' in request.POST:
        links = {}
        txt = []
        px = []
        spid = request.session['spid']
        c = request.POST.get('error')
        request.session['c'] = c
        cx = re.sub(r"\s([?.!',](?:\s|$))", r"\1", c)
        cx = cx.replace(" '","'")
        for a in new_dict[spid][c]:
            obj = SomeObject()
            obj.args = {spid:{c:{a}}}
            ob = SomeObject.objects.filter(args=obj.args).count()
            fla = 0
            links[a] = ob
            a = a.split("_")
            URL="https://en.wikipedia.org/?curid="+a[0]
            ind = sd.bisect(int(a[0]))
            key = sd.iloc[ind]
            value = str(sd[key], 'utf-8')
            all_files = os.listdir("extracted/"+value+'/')
            temp = open("extracted/"+value+"/index.txt","rb")
            dic = {}
            for all in all_files:
                for line in temp:
                    (key, val1) = line.split()
                    dic[int(val1)] = key
            sdi = SortedDict((key, value) for key, value in dic.items())
            ind = sdi.bisect(int(a[0]))
            key = sdi.iloc[ind-1]
            val = str(sdi[key], 'utf-8')
            with bz2.open("extracted/"+value+"/"+val, "rt") as bz_file:
                p = []
                for line in bz_file:
                    if fla == 1:
                        if cx in line:
                            p.append(line.replace(cx,"<b>"+cx+"</b>"))
                    if doc in line:
                        n = re.search(" +id=\"(.*?)\"", line)
                        if n.group(1) == a[0]:
                            fla = 1
                            pp = re.search(" +title=\"(.*?)\"", line)
                            px.append(pp.group(1))
                        else:
                            fla = 0
            #ALTERNATE WAY IF YOU WANT TO GET TEXTS FROM ONLINE LINKS
            #r = requests.get(URL)
            #soup = BeautifulSoup(r.content, 'html5lib')
            #abc = soup.get_text().splitlines()
            #cx = re.sub(r"\s([?.!',](?:\s|$))", r"\1", c)
            #cx = cx.replace(" '","'")
            #px.append(soup.title.string)
            #p = [line for line in soup.get_text().splitlines() if cx in line]
            txt.append(p)
        link = OrderedDict(sorted(links.items(), key=lambda t: t[1], reverse=True))
        context = {'links': link , 'cols': cx, 'txt':txt, 'px':px}
        return render(request, "search.html", context)
    if 'store' in request.POST:
        st = request.POST.getlist('recommendations')
        spid = request.session['spid']
        c = request.session['c']
        for s in st:
            for a in new_dict[spid][c]:
                if a == s:
                    obj = SomeObject()
                    obj.args = {spid:{c:{a}}}
                    obj.user = request.user
                    if SomeObject.objects.filter(args=obj.args, user=obj.user).exists() == False:
                        mission = "Thanks for your feedback"
                        obj.save()
                    else:
                        mission = "Already Exists"
        context = {'mission': mission}
        return render(request, "search.html", context)
    spid = request.session['spid']
    co = {}
    for c in new_dict[spid]:
        f = 0
        e = 0
        for a in new_dict[spid][c]:
            f = f + 1
            obj = SomeObject()
            obj.args = {spid:{c:{a}}}
            ob = SomeObject.objects.filter(args=obj.args).count()
            e = e + ob
        co[c] = [f, e]
    if 'alphabet' in request.POST:
        col = OrderedDict(sorted(co.items(), key=lambda t: t[0]))
    if 'frequency' in request.POST:
        col = OrderedDict(sorted(co.items(), key=lambda t: t[1][0], reverse=True))
    if 'marked' in request.POST:
        col = OrderedDict(sorted(co.items(), key=lambda t: t[1][1], reverse=True))
    context = {'col': col}
    return render(request, "search.html", context)

def login(request):
    context={}
    return render(request, "login.html", context)


def logout(request):
    context={}
    return render(request, "login.html", context)
