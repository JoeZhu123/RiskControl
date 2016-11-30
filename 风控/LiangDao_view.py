__author__='Joe'
#._*_coding:utf-8_*_
import redis
import sys
from django.shortcuts import render#MVC
from django.http import HttpResponse#NOT MVC
from django.shortcuts import render_to_response
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己mdl_LiangDao_dict的存放路径
from mdl_LiangDao_dict import *
    
def index(request):
    return render(request, 'index.html')

	
def mdl_data_dict(request):
    data0=random.randint(0,99)
    data1=random.randint(0,99)
    data2=random.randint(0,99)
    alpha0=-6489.75
    combin0='IC20160815'
    r=render_to_response('index1.html',locals())
    return r
