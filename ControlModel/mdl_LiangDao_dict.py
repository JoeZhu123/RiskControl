__author__='Joe'
#._*_coding:utf-8_*_
import redis
import sys
sys.path.append("/home/calc4/Desktop/zhuxinger/mdl-1.7.0/mdl_client_api/redis_protocol/demo/python/")#mdl_shl1_msg_pb2 and mdl_szl1_msg_pb2 directory
import mdl_shl1_msg_pb2
import mdl_szl1_msg_pb2

def mdl_connect():
    print "connect to redis..."
    r = redis.Redis(host='xxx.xxx.x.xxx', port=xxxx, db=0)#xxx.xxx.x.xxx代表通联数据的IP,xxxx为其端口
    if r.execute_command('auth', 'mytoken') :
        print "redis auth succeeded"
    else :
        print "redis auth failed"
        sys.exit()
    p = r.pubsub()
    p.subscribe(['mdl.3.3.*', 'mdl.3.4.*', 'mdl.5.1.*', 'mdl.5.2.*', 'mdl.2.4.*'])
    print "receiving message..."
    return p
class mdl_base:
    UpdateTime=0
    ID=0
    Name=0
    def mdl_time_str(self,x):
        return "%02d:%02d:%02d.%03d" % (x % 1000000000 / 10000000, x % 10000000 / 100000, x % 100000 / 1000, x % 1000)

    def mdl_float_str(self,x):
        return "%f" % (x.Value / float(x.DecimalShift))

    def mdl_int_str(self,x):
        return "%d" % (x)

class Stock(mdl_base):
    LastPrice=0
    PreCloPrice=0
    Volume=0
    def on_shl1_equity_msg(self,data):
        msg = mdl_shl1_msg_pb2.Equity()
        msg.ParseFromString(data)
        self.ID=msg.SecurityID
        self.Name=msg.UpdateTime
        self.LastPrice=msg.LastPrice
        self.PreCloPrice=msg.PreCloPrice
        self.Volume=msg.Volume
        return self
    def on_szl1_stock_msg(self,data):
        msg = mdl_szl1_msg_pb2.SZL1Stock()
        msg.ParseFromString(data)
        self.ID=msg.SecurityID
        self.Name=msg.UpdateTime
        self.LastPrice=msg.LastPrice
        self.PreCloPrice=msg.PreCloPrice
        self.Volume=msg.Volume
        return self

class Index(mdl_base):
    LastIndex=0
    PreCloseIndex=0
    def on_shl1_indexes_msg(self,data):
        msg = mdl_shl1_msg_pb2.Indexes()
        msg.ParseFromString(data)
        self.ID=msg.IndexID
        self.Name=msg.UpdateTime
        self.LastIndex=msg.LastIndex
        self.PreCloseIndex=msg.PreCloseIndex
        return self
    def on_szl1_index_msg(self,data):
        msg = mdl_szl1_msg_pb2.SZL1Index()
        msg.ParseFromString(data)
        self.ID=msg.IndexID
        self.Name=msg.UpdateTime
        self.LastIndex=msg.LastIndex
        self.PreCloseIndex=msg.PreCloseIndex
        return self


def Dictionary(item,stock,index,dictionary):
    if str(item['type']) == 'message':
        channel = str(item['channel'])
        if channel[0:8] == "mdl.3.3.":
            index=index.on_shl1_indexes_msg(item['data'])
            dictionary[index.ID]=index
            print "%s %s %s" % (index.ID,index.mdl_float_str(index.LastIndex),index.mdl_float_str(index.PreCloseIndex))
            return True
        elif channel[0:8] == "mdl.3.4.":
            stock=stock.on_shl1_equity_msg(item['data'])
            dictionary[stock.ID]=stock
            print "%s %s %s %d" % (stock.ID,stock.mdl_float_str(stock.LastPrice),stock.mdl_float_str(stock.PreCloPrice),stock.Volume)
            return True
        elif channel[0:8] == "mdl.5.1.":
            index=index.on_szl1_index_msg(item['data'])
            dictionary[index.ID]=index
            print "%s %s %s" % (index.ID,index.mdl_float_str(index.LastIndex),index.mdl_float_str(index.PreCloseIndex))
            return True
        elif channel[0:8] == "mdl.5.2.":
            stock=stock.on_szl1_stock_msg(item['data'])
            dictionary[stock.ID]=stock
            print "%s %s %s %d" % (stock.ID,stock.mdl_float_str(stock.LastPrice),stock.mdl_float_str(stock.PreCloPrice),stock.Volume)
            return True
        elif channel[0:8] == "mdl.2.4.":
            print "heart beat"
            return False
        else:
            print "unknown channel: %s" % (channel)
            return False
