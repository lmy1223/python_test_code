
import MySQLdb  
import time

conn = MySQLdb.Connection(host="localhost", user="root", passwd="", charset="UTF8")
conn.select_db('logintest')
cursor = conn.cursor ()  

'''cursor.execute (""" 
    CREATE TABLE login  
    ( 
        loginName CHAR(20), 
        loginPassword CHAR(50)
    ) 
    """)
'''
testData = []
for number in range (0,10):
    loginName = 'aaaaaaaaaabbb' + str(number)
    loginPassword = 'aaaaaaaaaabbb' + str(number)
    tmp = (loginName,loginPassword)
    testData.append(tmp)
 
sql = "insert into login(loginName,loginPassword) values(%s,%s)"   
    try :
        cursor.execute (sql ,(loginName,loginPassword))
        conn.commit()

    except :
        conn.rollback()
sql = "select * from login where (loginName =(%s) and loginPassword =(%s))"

print beforTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

for number in range (0,1000000):
    a = 'aaaaaaaaaabbb' + str(number)
    b = 'aaaaaaaaaabbb' + str(number)

    try:
        cursor.execute(sql,(a,b))
        results = cursor.fetchall()
        for row in results:
            loginName = row[0]
            loginPassword = row[1]
            print "loginName=%s,loginPassword=%s" % \
                (loginName,loginPassword)
    except:
        print "Error: unable to fecth data"
''' 
   try :
        cursor.execute (sql ,(a,b))
        conn.commit()

    except :
        conn.rollback()
'''



print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
conn.commit()  
cursor.close ()  
conn.close ()  









