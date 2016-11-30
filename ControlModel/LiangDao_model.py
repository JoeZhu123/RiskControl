__author__='Joe'
#._*_coding:utf-8_*_
import sys
import numpy
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your mdl_LiangDao_dict.py 's directory
from mdl_LiangDao_dict import *
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your LiangDao_controller.py 's directory
from LiangDao_controller import *
from LiangDao_db import *

#Combination Algorithm:
#Alpha tracking algorithm
class Alpha():
    S_Share=0
    S_Shares=0
    I_Share=0
    S_I=0
    S_I_Point=0
    S_I_Percent=0
    Market_Value=0
    Market_Values=0
    def Alpha_algorithm(self,combin,dictionary,stocks,stocks_volume,index,I_Multiplier):
        for s in stocks:
            self.S_Share=(float(dictionary[s].LastPrice.Value) - float(dictionary[s].PreCloPrice.Value))*(stocks_volume[s])
            self.S_Shares=self.S_Shares+self.S_Share
            self.Market_Value=dictionary[s].PreCloPrice.Value*stocks_volume[s]
            self.Market_Values=self.Market_Values+self.Market_Value
        self.I_Share=(dictionary[index].LastIndex-dictionary[index].PreCloseIndex)*I_Multiplier
        self.S_I=self.S_Shares-self.I_Share
        self.S_I_Point=self.S_I/I_Multiplier
        self.S_I_Percent=self.S_I/(self.Market_Values)
        combin.data0=self.S_I
        combin.data1=self.S_I_Point
        combin.data2=self.S_I_Percent
        combin.alpha_basis=-6489
        return combin



