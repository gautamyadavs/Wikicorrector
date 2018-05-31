from django.shortcuts import render
#from .forms import ListForm
from django.template.context import RequestContext
import pickle
import urllib.request
from .models import SomeObject
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
import re


pickle_off = open("/Users/gautam/Desktop/data.pickle","rb")
new_dict = pickle.load(pickle_off)

# Create your views here.
@login_required
def index(request):
    #data = {'Hyder Consulting': {'Freeman Fox': {'3212047_2_1'}, 'Freeman Fox & Partners': {'153761_8_0', '35603633_1_1', '1145603_1_1', '15619635_2_1', '709239_9_1', '30247811_2_0', '957768_4_0', '1145603_3_0', '20819903_9_1', '4096049_5_1', '2654362_0_1', '1790554_3_0', '382373_4_2', '13771451_2_0', '35952404_5_4', '11226604_1_1', '2568306_10_0', '20574057_3_0', '542710_7_1'}, 'Freeman Fox and Associates': {'1786680_12_0'}, 'Hyder Consulting': {'153761_8_0', '52485007_2_0', '20819903_13_1', '18651014_7_6', '44181442_5_0', '4405885_10_1', '10103814_5_1', '794957_33_0', '1625344_3_1', '12034777_9_1', '20819903_9_2', '1790319_1_2', '11503084_12_2', '5343555_15_0', '37511750_10_1', '1790554_3_0', '144983_17_1', '30861477_4_1', '52811853_2_0', '4405885_7_0'}, 'Hyder Consultants': {'355863_7_1'}, 'John Taylor & Sons': {'35952404_4_0', '35952404_0_3'}, 'Freeman Fox and Partners': {'144607_6_1', '2817744_4_0'}, 'W. & J. Taylor': {'2481728_15_3'}}, 'John Taylor (doctor)': {'John Taylor , M.D.': {'33951086_1_0'}, 'Joseph Taylor': {'33951002_1_0'}, 'John Taylor': {'30280189_1_0', '26536726_2_0'}}, 'John Taylor, Baron Kilclooney': {'John Taylor , Baron Kilclooney': {'4333462_59_2'}, 'Lord Kilclooney': {'9042915_1_0', '5463506_0_3', '18616244_4_4', '25078814_9_1', '4195514_0_4', '3776350_1_0'}, 'John D Taylor': {'16007435_3_0'}, 'John Taylor': {'229108_12_0', '2884380_3_2', '9089974_1_3', '146032_16_5', '4084422_30_0', '415673_9_0', '1873448_5_2', '415673_1_3', '52016785_3_0', '3576146_2_1', '9150644_3_0', '2497925_18_1', '866954_9_0', '7192544_8_0', '31893332_7_0', '16684002_6_0', '14599206_4_0', '9861604_7_0', '70525_18_0', '1645584_3_3', '866954_8_2', '2935740_4_1', '4775295_4_1', '7452206_1_0', '9089974_2_10', '16079743_1_2', '24166896_2_0'}}, 'John Taylor (bishop of Sheffield)': {'F J Taylor': {'1849543_6_8'}}, 'John Taylor (Mormon)': {'President John Taylor': {'3082429_3_0'}, 'her husband': {'17301752_2_2'}, 'President Taylor': {'35930323_3_4'}, 'John': {'4740959_3_4'}, 'John Taylor': {'6157514_3_2', '177459_0_0', '1397387_4_3', '35600224_5_4', '5942_24_1', '1063287_2_1', '670655_9_2', '10844087_4_0', '1055983_12_0', '1072762_15_1', '948164_6_2', '407740_10_3', '936989_6_2', '32085048_11_3', '2408771_5_4', '845910_6_1', '21065_9_2', '14160749_1_0', '3115208_3_0', '26337808_8_1', '10766152_4_1', '40308068_2_1', '10086110_7_0', '24475_63_3', '419037_23_0', '14352046_22_7', '19473742_4_0', '936989_0_4', '2609373_3_3', '25485663_2_1', '11144714_2_1', '15872404_42_0', '3680124_4_1', '26777467_2_0', '14677082_1_0', '1491174_4_2', '1014483_0_0', '3018281_6_1', '50553690_17_3', '3683470_3_3', '20403876_29_2', '2899869_141_0', '703932_8_2', '3121044_1_0', '1072531_4_0', '52413830_6_4', '435787_7_0', '20299762_4_1', '18183004_19_4', '13847997_6_0', '35600224_10_1', '3700461_1_1', '328088_3_3', '35600224_3_3', '45170243_1_0', '137077_8_0', '2929315_1_0', '15550448_2_0', '1638962_8_0', '49882002_6_3', '28933572_3_1', '1783363_4_0', '22137322_5_0', '307496_50_0', '30090366_1_7', '26566642_6_7', '24263505_11_0', '1117127_11_0', '29290448_6_2', '22851993_15_3', '38585548_4_1', '27544427_2_0', '11188641_4_0', '14757847_13_3', '14267584_4_1', '442718_11_0', '13221945_0_0', '6157514_5_0', '11162096_7_2', '639575_22_0', '6305642_17_0', '2063169_4_2', '16969810_2_1', '32544608_7_1', '19230475_30_3', '11553453_9_1', '11194957_6_3', '41695422_7_0', '1074627_5_0', '44277650_3_0', '1843643_2_0', '2040605_6_0', '5792321_19_1', '13847997_4_2', '26013486_2_2', '431308_9_3', '2330251_18_0', '1072778_7_4', '1673611_5_1', '2901235_3_2', '183660_23_4', '23850991_2_2', '1352778_49_2', '94684_6_0', '5810892_20_1', '13005866_0_0', '32496048_2_1', '636946_3_1', '26566642_12_2', '5290240_3_0', '12701908_0_0', '54667172_4_2', '1434495_40_2', '9560087_6_1', '13656486_3_1', '37882492_1_0', '11236978_2_0', '13410007_1_0', '384795_4_2', '35600224_6_11', '6157514_0_2', '10921421_4_1', '2893690_4_2', '12883059_1_4', '49183999_1_1', '2548097_17_0', '13011076_3_2', '24475_60_1', '436845_1_8', '4809391_17_6', '12790315_3_1', '42498289_11_8', '5810892_74_2', '9606500_0_0', '12908516_5_0', '28933572_7_2', '10903341_7_0', '14776403_5_0', '9606500_11_0', '4031060_3_0', '4003726_0_0', '435787_16_0', '37733241_9_0', '431949_18_0', '6185532_6_2', '32495959_20_3', '12804784_3_0', '903085_9_0', '1038104_0_0', '19440495_2_2', '36266237_4_1', '29956440_1_2', '137071_20_0', '28140821_1_0', '3103704_6_4', '17324173_0_0', '1783358_16_1', '183660_41_0', '676244_6_1', '45170243_7_1', '17301183_0_1', '413466_8_0', '2773067_9_1', '42498289_18_0', '12995584_0_0', '2908031_8_0', '10845858_2_1', '246903_12_0', '3082429_1_4', '28972501_6_2', '13032539_4_2', '137212_8_1', '394889_7_0', '11553268_0_1', '407740_3_0', '5290240_1_1', '35829931_1_0', '12861333_5_0'}, "John Taylor 's": {'32495959_35_0', '2416523_9_1', '435787_9_5', '12702190_0_2'}}, 'John Taylor (Scottish politician)': {'John Taylor': {'25067525_1_0'}}, '1998–99 Scottish First Division': {'promotion': {'2590357_7_1'}, 'winning the First Division': {'8436004_3_0'}, '1999': {'25891866_1_0', '25908545_1_0'}}, 'John Lloyd Taylor': {'John Taylor': {'40036311_5_3', '17086300_4_0', '18726486_0_2', '18726486_2_5'}}, 'Dr. John Taylor': {'Dr. John Taylor': {'52754301_1_4'}}, 'John Taylor (VC)': {'John Taylor': {'1179420_4_1', '1219207_2_1'}}, 'Charles John Taylor': {'Charles Taylor': {'39278731_2_0'}, 'Charles John Taylor': {'3058675_3_2', '1268690_1_2', '16567242_6_1', '24536829_5_2', '34489358_3_0', '3054015_4_2'}}, 'John Taylor (Australian rules footballer)': {'John Taylor': {'22314618_3_3'}}}
    #with open('/Users/gautam/Desktop/data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
    #    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
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

@login_required
def search(request):
    global new_dict
    if 'selection' in request.POST:
        spid = request.POST.get('selection')
        request.session['spid'] = spid
        context = {'col': new_dict[spid]}
        return render(request, "search.html", context)
    if 'error' in request.POST:
        links = []
        txt = []
        px = []
        spid = request.session['spid']
        c = request.POST.get('error')
        request.session['c'] = c
        for a in new_dict[spid][c]:
            links.append(a)
            a = a.split("_")
            URL="https://en.wikipedia.org/?curid="+a[0]
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            abc = soup.get_text().splitlines()
            cx = re.sub(r"\s([?.!',](?:\s|$))", r"\1", c)
            cx = cx.replace(" '","'")
            px.append(soup.title.string)
            p = [line for line in soup.get_text().splitlines() if cx in line]
            txt.append(p)
        context = {'links': links , 'cols': cx, 'txt':txt, 'px':px}
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
                        obj.save()
        context = {}
        return render(request, "search.html", context)


def login(request):
    context={}
    return render(request, "login.html", context)


def logout(request):
    context={}
    return render(request, "login.html", context)
