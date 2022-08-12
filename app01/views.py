from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
import requests
from lxml import etree
from app01.models import UserInfo
from app01.models import Department


# Create your views here.

def index(request):
    return render(request, "index.html")


def user_list(request):
    # 会根据app的注册顺序逐一去各个app下得templates文件夹下寻找user_list.html文件
    # UserInfo.objects.create(name='user1',password='123456',age=23)
    # UserInfo.objects.create(name='user2', password='123456', age=32)
    # UserInfo.objects.create(name='user3', password='123456', age=35)
    # UserInfo.objects.create(name='user4', password='123456', age=25)
    return render(request, "user_list.html")


def user_add(request):
    if request.method == 'GET':
        return render(request, "user_add.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        userage = request.POST.get("userage")
        UserInfo.objects.create(name=username, password=password, age=userage)
        return redirect("/user/info")


def tpl(request):
    name = "rongyin"
    roles = ["管理员", "ceo", "保安"]
    user_info = {"name": "rongyin", "salary": 10000, "role": "ceo"}
    data_list = [
        {"name": "rongyin", "salary": 10000, "role": "ceo"},
        {"name": "liuling", "salary": 10000, "role": "ceo"},
        {"name": "rongxin", "salary": 10000, "role": "ceo"}
    ]
    return render(request, "tpl.html", {"name": name, "roles": roles, "user_info": user_info, "data_list": data_list})


def news(request):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Connection': 'keep-alive'
    }
    res = requests.get("https://movie.douban.com/chart", headers=headers)
    tree = etree.HTML(res.text)
    li_list = tree.xpath("//div[@class='article']//div[@class='pl2']/a/span/text()")
    return render(request, "news.html", {"list": li_list})


def user_info(request):
    data_list = UserInfo.objects.all()
    return render(request, 'user_info.html', {"data_list": data_list})


def user_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/info")
