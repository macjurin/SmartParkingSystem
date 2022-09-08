from p1 import *
from p2 import *
from p3 import *
from p4 import *
from p5 import *
from p6 import *
import threading as t
import mysql.connector as mysql
from datetime import datetime


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "parking_system"
)
"""
def latitude_to_string(n):
    k=n[:2:]+"."+n[3:5:]+"."n[6:8]+"."+n[9:]
    return k

def longitude_to_string(n):
    k=n[:2:]+"."+n[3:5:]+"."n[6:8]+"."+n[9:]
    return k

def string_to_latitude(n):
    k=n[:2:]+"°"+n[3:5:]+"\'"n[6:8]+"\""+n[9:]
    return k   

def string_to_longitude(n):
    k=n[:2:]+"°"+n[3:5:]+"\'"n[6:8]+"\""+n[9:]
    return k
"""

def entry():
    while True:
        irsensor(18)
        p=lpr(0)
        #Find nearest slot
        cursor = db.cursor()
        query = "SELECT Id,lon,lat FROM location WHERE Id = (SELECT MIN(Id) FROM location WHERE status = 'NA')"
        cursor.execute(query)
        records = cursor.fetchall()
        i = records[0]

        query1="SELECT Email FROM Car_Allocate WHERE Car_Number = %s"
        cursor.execute(query1,p)
        records = cursor.fetchall()
        e = records[0]
        msg=str(i[1]+","+i[2])

        sendEmail(e[0],msg)

        mycursor = db.cursor()

        # datetime object containing current date and time
        t = datetime.now()
        sql1 = "INSERT INTO Records (Email,Car_Number,Id,In_time ) VALUES (%s, %s,%s,%s)"
        rd=(str(e[0]),p,int(i[0]),t)
        mycursor.execute(sql1,rd)
        print(mycursor.rowcount, "details inserted")


        sql = "UPDATE Car_Allocate SET Car_Status = %s WHERE Car_Number=%s AND Car_exit='NE'"
        data = ("A", p)
        mycursor.execute(sql, data)
        print(mycursor.rowcount, "record(s) affected")

        sql2 = "UPDATE `location` SET status = %s WHERE Id=%s"
        data1 = ("A", int(i[0]))
        mycursor.execute(sql2, data1)
        print(mycursor.rowcount, "record(s) affected")

        query2 = "SELECT Pin1,Pin2 FROM `Pin` WHERE Id = %s AND `Type`=%s"
        pd = (int(i[0]), "motor")
        cursor.execute(query2, pd)
        records = cursor.fetchall()
        p1 = records[0]
        drot(int(p1[0]),int(p1[1]),1)
        drot(11,12,1)
        irsensor2(19)
        drot(11,12,0)



def exit():
    cursor1 = db.cursor()
    query2 = "SELECT Pin1,`Id` FROM `Pin` WHERE `Type`=%s"
    cursor1.execute(query2, "irsensor")
    records = cursor1.fetchall()

    while True:
        for i in records:
            c=irsensor1(i[0])
            if(c==0):
                cursor2 = db.cursor()
                q2 = "SELECT In_time FROM Record WHERE `Id`=%s"
                cursor2.execute(q2,i[1])
                r2 = cursor2.fetchall()
                it = r2[0]
                ot = datetime.now()
                ft = ot - it[0]
                if(ft>60):
                    query2 = "SELECT Pin1,Pin2 FROM `Pin` WHERE `Id`=%s AND `Type`=%s"
                    pd=(i[0],"motor")
                    cursor1.execute(query2,pd)
                    r3 = cursor1.fetchall()
                    mi1 = r3[0]
                    drot(mi1[0],mi1[1],1)

                    cursor = db.cursor()
                    query = "UPDATE `location` SET status = %s WHERE `Id`=%s"
                    pd = ("NA", i[1])
                    cursor.execute(query, pd)
                    print(cursor.rowcount, "record(s) affected")

                    mycursor = db.cursor()

                    # datetime object containing current date and time

                    sql1 = "UPDATE `Records` SET Out_time = %s WHERE `Id`=%s"
                    rd = (ot,i[1])
                    mycursor.execute(sql1, rd)
                    print(mycursor.rowcount, "details inserted")
                    #sendemail

                    sql = "UPDATE Car_Allocate SET Car_exit = %s WHERE `Id`=%s"
                    data = ("E",i[1])
                    mycursor.execute(sql, data)
                    print(mycursor.rowcount, "record(s) affected")
            else:
                cursor2 = db.cursor()
                q2 = "SELECT Car_Status FROM Car_Allocate WHERE `Id`=%s"
                cursor2.execute(q2, i[1])
                r2 = cursor2.fetchall()
                status = r2[0]
                if(status=="A"):
                    q3= "UPDATE Car_Allocate SET Car_Reach='R' WHERE `Id`=%s"
                    cursor2.execute(q3,i[1])
                    print(cursor2.rowcount, "record(s) affected")

t.Thread(target=entry).start()
t.Thread(target=exit).start()


