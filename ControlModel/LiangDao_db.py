#.-*- coding: UTF-8 -*-
import redis
import sys
import MySQLdb
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your LiangDao_model.py 's directory
from mdl_LiangDao_dict import *
sys.path.append("/home/calc4/RiskControl/ControlModel/")#your LiangDao_model.py 's directory
from LiangDao_model import *
from django.db import models
from django.http import HttpResponse
from ControlModel.models import *

reload(sys)
sys.setdefaultencoding('utf-8')

def dbstock(request):
    response=""
    response1=""
    combin_stocks = DB_Stock.objects.all()
    for var in combin_stocks:
        print var.ID
    #response1+=var.ID+" "
    #response=response1
    #response1=DB_Stock.objects.filter(ID='603818')
    #stock1=DB_Stock(ID='603818',Name='qumeijiaju',Volume=900)	
    #stock1.save()
    return HttpResponse("<p ok /p>")

class LiangDao_db():
    date_time=0
    def sql_connect(self):
        #start to connect MySQL data base
        db = MySQLdb.connect("localhost","root","123456","liangdao" )
        cursor = db.cursor()
    def sql_disconnect(self):
        #Disconnect MySQL data base
        db.close()
        cursor = db.cursor()

    def insert_combination(self,combination):
        sql="""INSERT INTO COMBINATION(CombinationName,
            STOCKS,INDEXES,SEX,INCOME)
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
        sql="SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" %(1000)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            #if error occurred, database rollback
            db.rollback()
            print "Error:unable to fetch data"
        return null
    def delete_combination(self,combination):
        sql="DELETE FROM EMPLOYEE WHERE AGE>'%d'" %(20)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            #if error occurred, database rollback
            db.rollback()
            print "Error:unable to fetch data"
        return null
    def update_combination(self,combination):
        sql="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%c'" %('M')
        try:
            cursor.execute(sql)
            db.commit()
        except:
            #if error occurred, database rollback
            db.rollback()
            print "Error:unable to fetch data"
        return null

    def insert_dictionary(self,dictionary):
        return null
    def get_dictionary(self,dictionary):
        return null
    def delete_dictionary(self,dictionary):
        return null
    def update_dictionary(self,dictionary):
        return null
