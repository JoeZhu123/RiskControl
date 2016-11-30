__author__='Joe'
#._*_coding:utf-8_*_
import sys
import numpy
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己mdl_LiangDao_dict的存放路径
from mdl_LiangDao_dict import *
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己LiangDao_controller的存放路径
from LiangDao_controller import *
from LiangDao_db import *

#多种组合算法：
#Alpha tracking algorithm
class Alpha:
    S_Share=0
    S_Shares=0
    I_Share=0 
    S_I=0
    S_I_Point=0
    S_I_Percent=0
    Market_Value=0
    Market_Values=0
    def Alpha_algorithm(self,stocks,indexes,I_Multiplier):
        self.S_Share=(Stock.LastPrice - Stock.PreCloPrice)*float(Stock.Volume)
        self.S_Shares=self.S_Shares+self.S_Share
        self.I_Share=(Index.LastIndex-Index.PreCloseIndex)*I_Multiplier
        self.Market_Value=Stock.PreCloPrice*Stock.Volume
        self.Market_Values=self.Market_Values+self.Market_Value
        self.S_I=self.S_Shares-self.I_Share
        self.S_I_Point=self.S_I/I_Multiplier
        self.S_I_Percent=self.S_I/(self.Market_Values+1)        
        Output_List=[self.S_I,self.S_I_Point,self.S_I_Percent]
        return Output_List

    def Alpha_calc(self,dictionary,stocks,indexes):
        dictionary={}#one data dictionary
        output_list=self.Alpha_algorithm(dictionary[stocks],dictionary[indexes],I_Multiplier)
        print "%f %f %f " % ((output_list[0]), (output_list[1]),(output_list[3]))#self.mdl_float_str
        return output_list

class CombinationManager:
    I_Multipliers=[]#合约乘数
	Stocks=[]#组合中的多支股票
	Indexes=[]#组合中的多支指数
	CombinationName=''#组合名称
	def __init__(self,stocks,indexes):
      self.I_Multipliers=[200,300,300]
	  self.Stocks=stocks
	  self.Indexes=indexes
    def CombinationChoice(self,Combinations):#Combinations是从表单里选择的多个组合；例如['IC20160815组合','IC20160810组合']
		aResults={}
        for x in Combinations:
			#每个组合的CombinationName，Indexes，Stocks，I_Multipliers从数据库里获取
            aResults[x] = Alpha().Alpha_calc(x,stock_names,index_names)
		return aResults
	def CombinationAdd(self,):
        for x in Combinations:
            aResult = Alpha().Alpha_calc(x,stock_names,index_names)