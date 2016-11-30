__author__='Joe'
#._*_coding:utf-8_*_
import redis
import sys
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your LiangDao_model.py 's directory
from LiangDao_model import *
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your LiangDao_db.py 's directory
from LiangDao_db import *
from ControlModel.models import *

class Combin():
    CombinName=''
    data0 = 0
    data1 = 0
    data2 = 0
    alpha_basis = 0
#Model Controller(To manage combination)
class CombinationManager():
    I_Multipliers=[]
    Stocks=[]
    Stocks_volume={}
    Indexes=[]
    CombinationNames=[]
    def __init__(self):
        #query combin from database
        combin_lists = DB_Stock .objects.all()
        for com in combin_lists:
            if com.Combin not in self.CombinationNames:
                self.CombinationNames.append(com.Combin)
        self.I_Multipliers=[200,300,300]
        self.Indexes=['000300','000905']
    def ChooseCombination(self,dictionary,Combination):#Combinations:such as['IC20160815','IC20160810']
        combin=Combin()
        dictionary_temp={}
        combin.CombinName=Combination
        combin_stocks = DB_Stock.objects.filter(Combin=combin.CombinName)
        for var in combin_stocks:
            self.Stocks.append(var.ID)
            self.Stocks_volume[var.ID]=var.Volume
        for s in self.Stocks:
            dictionary_temp[s]=dictionary[s]
        index_temp = self.Indexes[0]
        if Combination[0:1]=='IF':
            index_temp=self.Indexes[0]
            print 'SH000300'
        elif Combination[0:1]=='IC':
            index_temp=self.Indexes[1]
            print 'SH000905'
        combin = Alpha().Alpha_algorithm(combin, dictionary_temp,self.Stocks,self.Stocks_volume,index_temp,self.I_Multipliers[0])
        return combin
    def AddCombination(self):
        return 0
