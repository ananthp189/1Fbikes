# Database

# 1. Customer information:
# ID                 integer  PRIMARY KEY  
# UserName   text
# Password    text
# Tel
# Bankcard
# usertype  (0 means normal, 1 means prime, 2 means operater, 3 means manager)
# uGPS
# uarea
# Balance


# 2. Bike information:
# bID       integer  PRIMARY KEY 
# bstatus    (0 means good, 1 means good)
# bGPS
# barea
# bpassword
# busage      (0 means unuse, 1 means using)

# 3. Payment information:
# pID       integer PRIMARY KEY 
# ID
# bID
# starttime
# endtime
# duration
# oribill
# discount
# startGPS
# endGPS

import random as r
import pymysql 
import datetime
import time

############################ Customer Information Database ############################

# Creat random name
first=('Liam','Noah','Oliver','William','Elijah','James','Benjamin','Lucas','Mason','Ethan','Alexander','Henry','Jacob','Michael','Daniel','Logan','Jackson','Sebastian','Jack')
last=('Smith','Johnson','Williams','Brown','Davis','Miller','Taylor','Martin','Moore','Walker','Clark','Scott','King')
name=[]
for i in range(100):  
  name1=r.choice(first)+" "+r.choice(last) 
  name2=name1.rstrip()
  if name2 not in name:
    name.append(name2)

# Create random password
passwd1 = ('qwe', 'asd', 'wasd', 'abc', 'zxc')
passwd2 = ('1234', '5678', '147', '258', '741', '312')
passwd3 = ('!', '@', '#', '$', '%', '!!')
passwd = []
for i in range(100):
    password = r.choice(passwd1) + r.choice(passwd2) + r.choice(passwd3)
    if password not in passwd:
        passwd.append(password)



# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='project')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS customer_info(
    ID int PRIMARY KEY,
    UserName text,
    Password text,
    renttime text,
    Tel text,
    Bankcard text,
    usertype text,
    Balance text);""")


# Insert the data:
for i in range(len(name)):            # import 100 customer information
  pw = r.choice(passwd)
  rt = str(r.randint(0, 100))
  tel_num = str(r.randint(1000000000,9999999999))
  bankcard_num = str(r.randint(1000000000000000,9999999999999999))
  typelist = ("0", "0", "0", "0", "0", "0", "1", "1", "2", "3")
  u_ty = r.choice(typelist)
  balance = str(r.randint(0, 100))
  cur.execute("insert into customer_info(ID, UserName, Password, renttime, Tel, Bankcard, usertype, Balance) values(%s,%s,%s,%s,%s,%s,%s,%s)",(i+1, name[i], pw, rt, tel_num, bankcard_num, u_ty, balance))

cur.execute('select * from customer_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()





############################ Bike Information Database ############################

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='project')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS bike_info(
    bID int PRIMARY KEY,
    bstatus text,
    bGPS text,
    barea text,
    bpassword text,
    busage text);""")


# Insert the data:
for i in range(500):        # import 500 bikes information
  status_list = ("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1")
  bs = r.choice(status_list)
  area_list = ("A", "B", "C", "D")
  ba = r.choice(area_list)
  bp = str(r.randint(1000, 9999))
  usage_list = ("0", "0", "0", "1")
  bu = r.choice(usage_list)
  cur.execute("insert into bike_info(bID, bstatus, barea, bpassword, busage) values(%s,%s,%s,%s,%s)",(i+1, bs, ba, bp, bu))

cur.execute('select * from bike_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()




########################## payment information Database #############################

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='project')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS pay_info(
    pID integer PRIMARY KEY,
    ID text,
    bID text,
    starttime text,
    endtime text,
    duration text,
    oribill text,
    discount text,
    startGPS text,
    endGPS text);""")


# Insert the data:
for i in range(1000):        # import 1000 payment information
  a1=(2020,1,1,0,0,0,0,0,0)
  a2=(2021,2,1,23,59,59,0,0,0)
  start=time.mktime(a1)
  end=time.mktime(a2)
  t=r.randint(start,end)
  date_touple=time.localtime(t)
  starttime1 = time.strftime("%Y-%m-%d %H:%M:%S",date_touple)
  starttime = datetime.datetime.strptime(starttime1, "%Y-%m-%d %H:%M:%S")
  duration = int(r.randint(1, 600))
  endtime = (starttime + datetime.timedelta(minutes = duration)).strftime("%Y-%m-%d %H:%M:%S")

  cur.execute("insert into pay_info(pID, ID, bID, starttime, endtime, duration) values(%s,%s,%s,%s,%s,%s)",(i+1, r.randint(1, 82), r.randint(1, 500), starttime, endtime, duration))

cur.execute('select * from pay_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()

