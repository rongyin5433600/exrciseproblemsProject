from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests
import json
from lxml import etree


# Create your views here.

def index(request):
    return render(request, "index.html")


def user_list(request):
    # 会根据app的注册顺序逐一去各个app下得templates文件夹下寻找user_list.html文件
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


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
