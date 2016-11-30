__author__='Joe'
#._*_coding:utf-8_*_
import re
import redis
import sys
import random
from django.shortcuts import render#MVC
from django.http import HttpResponse#NOT MVC
from django.shortcuts import render_to_response
sys.path.append("/home/calc4/RiskControl/ControlModel/")#
from mdl_LiangDao_dict import *
from LiangDao_controller import *

from django.http import HttpResponseRedirect
from django import forms
from ControlModel.models import *
from ControlModel.LiangDao_controller import *
from xlwt import *


reload(sys)
sys.setdefaultencoding('utf8')

class UploadFileForm(forms.Form):
	#datatitle=forms.CharField(max_length=50)
	datafile=forms.FileField()

def handle_uploaded_file(f):
	destination=open(f.name,'wb+')
	for chunk in f.chunks():
		destination.write(chunk.decode('gbk'))
	destination.close()

# Create your views here.    
def index(request):
	return render(request, 'index.html')

def index2(request):
	if request.method=="POST":
		#uf=UploadFileForm(request.POST,request.FILES)
		#if uf.is_valid():
		f=request.FILES['file']
		handle_uploaded_file(f)
		combin=(f.name).split('.')[0]
		stocks=[]
		length_lines=0
		check_box_list=[]
		check_box_list = request.POST.getlist("check_box_list")
		for chunk in f.chunks():
			lines=re.split('\n',chunk)
			length_lines=len(lines)
			for line in lines:
				l=line.split(' ')
				if len(l)<3:continue
				stock=Stock()
				stock.ID=l[0]
				stock.Name=l[1].decode('gbk')
				stock.Volume=l[2]
				stocks.append(stock)
				#insert stocks into database
				if len(check_box_list)==1:
					stockdb=DB_Stock(Combin=combin,ID=stock.ID,Name=stock.Name,Volume=stock.Volume)
					stockdb.save()
		print length_lines
		return render_to_response('index2.html',locals())
	else:
		uf=UploadFileForm()
	return render_to_response('index2.html',locals())

p=mdl_connect()
dictionary={}
def risk_data(request):
	stock=Stock()
	index=Index()
	combination=CombinationManager()
	combins=[]
	bool_flag=False
	for item in p.listen():
		bool_flag=Dictionary(item,stock,index,dictionary)
		for combinname in combination.CombinationNames:
			combins.append(combination.ChooseCombination(dictionary,combinname))
		if bool_flag == True:
			break
	print "%d" %(len(dictionary))
	r=render_to_response('index1.html',locals())
	return r


