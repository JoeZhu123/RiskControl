__author__='Joe'
#._*_coding:utf-8_*_
import redis
import sys
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己LiangDao_model的存放路径
from LiangDao_model import *
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己LiangDao_view的存放路径
from LiangDao_view import *
from LiangDao_db import *

#模型控制器(组合管理)：

class CombinationManager:
    I_Multipliers=[]#合约乘数
	Stocks=[]#组合中的多支股票
	Indexes=[]#组合中的多支指数
	CombinationName=''#组合名称
	def __init__(self,stocks,indexes):
      self.I_Multipliers=[200,300,300]
	  self.Stocks=stocks
	  self.Indexes=indexes
    def chooseCombination(self,Combinations):#Combinations是从表单里选择的多个组合；例如['IC20160815组合','IC20160810组合']
		aResults={}
        for x in Combinations:
			#每个组合的CombinationName，Indexes，Stocks，I_Multipliers从数据库里获取
            aResults[x] = Alpha().Alpha_calc(x,stock_names,index_names)
		return aResults
	def addCombination(self,):
        for x in Combinations:
            aResult = Alpha().Alpha_calc(x,stock_names,index_names)



