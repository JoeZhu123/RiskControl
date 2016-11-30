__author__='Joe'
#._*_coding:utf-8_*_
import redis
import sys
import MySQLdb
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己mdl_LiangDao_dict的存放路径
from mdl_LiangDao_dict import *
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/liangdao/mdL_data/")#这个要看自己LiangDao_model的存放路径
from LiangDao_model import *

reload(sys)
sys.setdefaultencoding('utf-8')

#将组合算法信息和mdl通联数据存储到数据库：
class LiangDao_db():
    date_time=0
    def sql_connect(self):
        #连接数据库及数据库的基本操作
        #start to connect MySQL data base
        db = MySQLdb.connect("localhost","root","123456","liangdao" )
        cursor = db.cursor()
    def sql_disconnect(self):
        #Disconnect MySQL data base
        db.close()
        cursor = db.cursor()      
        
    def insert_combination(self,combination):
        #向数据库中保存组合信息
        sql="""INSERT INTO COMBINATION(CombinationName,
            LAST_NAME,AGE,SEX,INCOME)
            VALUES('Mac','Mohan',20,'M',2000)"""
        try:
           cursor.execute(sql)
           db.commit()        
        except:
           #if error occurred, database rollback
           db.rollback()
           print "Error:unable to fetch data"
        return null
    def get_combination(self,combination):
        #从数据库中取出组合信息
		sql2="SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" %(1000)
        try:
           cursor.execute(sql)
           cursor.execute(sql1)
           db.commit()        
        except:
           #if error occurred, database rollback
           db.rollback()
           print "Error:unable to fetch data"
        return null
	def delete_combination(self,combination):
        #向数据库中保存组合信息
		sql4="DELETE FROM EMPLOYEE WHERE AGE>'%d'" %(20)
        try:
           cursor.execute(sql)
           cursor.execute(sql1)
           db.commit()        
        except:
           #if error occurred, database rollback
           db.rollback()
           print "Error:unable to fetch data"
        return null
    def update_combination(self,combination):
        #从数据库中取出组合信息
		sql3="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%c'" %('M')
        try:
           cursor.execute(sql)
           cursor.execute(sql1)
           db.commit()        
        except:
           #if error occurred, database rollback
           db.rollback()
           print "Error:unable to fetch data"
        return null
		
	def insert_dictionary(self,dictionary):
        #向数据库中保存股票字典
        return null
    def get_dictionary(self,dictionary):
        #从数据库中取出股票字典
        return null
    def delete_dictionary(self,dictionary):
        #向数据库中保存股票字典
        return null
    def update_dictionary(self,dictionary):
        #从数据库中取出股票字典
        return null
