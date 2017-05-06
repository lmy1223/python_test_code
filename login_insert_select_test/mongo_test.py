import pymongo
import time
import datetime
import random

from pymongo import *
conn= MongoClient("localhost", 27017)
db = conn.logintest
collection = db.login

for i in range(0,10000):
    u = dict(loginName = "aaaaaaaaaabbb" + str(i), loginPassword = "aaaaaaaaaabbb" + str(i))
    db.login.insert(u)

beforeTime = time.mktime (datetime.datetime.now().timetuple())
print  'Execute sql befor now time is : ' +str(beforeTime);

beforeTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print  'Execute sql befor now time is : ' +str(beforeTime);


b_list = range(0,1000000)
for j in random.sample(b_list, 1000000):
    db.login.find({'loginName':"aaaaaaaaaabbb" + str(j), 'loginPassword':"aaaaaaaaaabbb" + str(j)})
print db.login.find().count()

afterTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print  'Execute sql befor now time is : ' +str(afterTime);

afterTime = time.mktime (datetime.datetime.now().timetuple())
print  'Execute sql after now time is : ' +str(afterTime);

allExecuteTime = afterTime - beforeTime
print 'All time is : ' + str(allExecuteTime)

conn.close()