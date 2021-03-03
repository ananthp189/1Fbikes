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
# bstatus    (0 means good, 1 means broken)
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
for i in range(150):
    name1=r.choice(first)+" "+r.choice(last)
    name2=name1.rstrip()
    # if name2 not in name:
    name.append(name2)

# Create random password
passwd1 = ('qwe', 'asd', 'wasd', 'abc', 'zxc')
passwd2 = ('1234', '5678', '147', '258', '741', '312')
passwd3 = ('!', '@', '#', '$', '%', '!!')
passwd = []
for i in range(150):
    password = r.choice(passwd1) + r.choice(passwd2) + r.choice(passwd3)
    # if password not in passwd:
    passwd.append(password)

# Create random email
em1 = ('qaz', 'wsx', 'edc', 'abc', 'zxc')
em2 = ('1234', '5678', '147', '258', '741', '312')
em3 = ('!', '!!', '#', '$', '%', '!!')
em4 = ('gmail', 'hotmail', 'mail', 'msn', 'outlook')
em = []
for i in range(150):
    email = r.choice(em1) + r.choice(em2) + r.choice(em3) + "@" + r.choice(em4)+".com"
    if email not in em:
        em.append(email)

# Create random gps info
ugpsx = r.uniform(55.81, 55.95)




# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS customer_info(
#     ID int PRIMARY KEY,
#     UserName text,
#     Password text,
#     renttime text,
#     Tel text,
#     Bankcard text,
#     usertype text,
#     Balance text);""")


# Insert the data:
for i in range(len(name)):            # import 150 customer information
    pw = r.choice(passwd)
    rt = str(r.randint(0, 100))
    tel_num = str(r.randint(10000000,99999999))
    bankcard_num = str(r.randint(1000000000000,9999999999999))
    typelist = ("0", "0", "0", "0", "0", "1", "1", "1", "2", "3")
    u_ty = r.choice(typelist)
    balance = str(r.randint(0, 100))
    ugpsx = r.uniform(55.81, 55.95)
    ugpsy = r.uniform(-4.31, -4.0)
    em1 = r.choice(em)
    cur.execute("insert into customer_info(ID, UserName, Password, renttime, Tel, Bankcard, usertype, Balance, uGPSx, uGPSy, email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i+1011, name[i], pw, rt, tel_num, bankcard_num, u_ty, balance, round(ugpsx, 10), round(ugpsy, 10), em1))

cur.execute('select * from customer_info')
for s in cur.fetchall():
    print(s)
conn.commit()
cur.close()
conn.close()





############################ Bike Information Database ############################

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor() 
# cur.execute("""CREATE TABLE IF NOT EXISTS bike_info(
#     bID int PRIMARY KEY,
#     bstatus text,
#     bGPS text,
#     barea text,
#     bpassword text,
#     busage text);""")


# Insert the data:
for i in range(500):        # import 500 bikes information
  status_list = ("0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1")
  bs = r.choice(status_list)
  # area_list = ("A", "B", "C", "D")
  # ba = r.choice(area_list)
  bgpsx = r.uniform(55.81, 55.95)
  bgpsy = r.uniform(-4.31, -4.0)
  bp = str(r.randint(1000, 9999))
  usage_list = ("0", "0", "1", "1")
  bu = r.choice(usage_list)
  cur.execute("insert into bike_info(bID, bstatus, bGPSx, bGPSy, bpassword, busage) values(%s,%s,%s,%s,%s,%s)",(i+106, bs, round(bgpsx, 10), round(bgpsy, 10), bp, bu))

cur.execute('select * from bike_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()




########################## payment information Database #############################

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor() 
# cur.execute("""CREATE TABLE IF NOT EXISTS pay_info(
#     pID integer PRIMARY KEY,
#     ID text,
#     bID text,
#     starttime text,
#     endtime text,
#     duration text,
#     oribill text,
#     discount text,
#     startGPS text,
#     endGPS text);""")


# Insert the data:
for i in range(1000):        # import 1000 payment information
  a1=(2020,1,1,0,0,0,0,0,0)
  a2=(2021,2,25,23,59,59,0,0,0)
  start=time.mktime(a1)
  end=time.mktime(a2)
  t=r.randint(start,end)
  date_touple=time.localtime(t)
  starttime1 = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)
  starttime = datetime.datetime.strptime(starttime1, "%Y-%m-%d %H:%M:%S")
  d_list = (r.randint(5, 60), r.randint(1, 600))
  duration = int(r.choice(d_list))
  endtime = (starttime + datetime.timedelta(minutes = duration)).strftime("%Y-%m-%d %H:%M:%S")
  oribill = duration / 60 * 0.5
  discount = oribill * 0.8
  psgpsx = r.uniform(55.81, 55.95)
  psgpsy = r.uniform(-4.31, -4.0)
  pegpsx = r.uniform(55.81, 55.95)
  pegpsy = r.uniform(-4.31, -4.0)

  cur.execute("insert into pay_info(pID, ID, bID, starttime, endtime, duration, oribill, discount, startGPSx, startGPSy, endGPSx, endGPSy, pstatus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (i+2003, r.randint(1001, 1160), r.randint(110, 600), starttime, endtime, duration, round(oribill, 2), round(discount, 2), round(psgpsx, 10), round(psgpsy, 10), round(pegpsx, 10), round(pegpsy, 10), 1))

cur.execute('select * from pay_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()



# update the area information for bike

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor()

sqlA = "update bike_info set barea = 'A' where (bGPSx > 55.85 and bGPSx < 55.90) and (bGPSy > -4.26 and bGPSy < -4.15)"
sqlB = "update bike_info set barea = 'B' where (bGPSx > 55.88 and bGPSx < 55.95 and bGPSy > -4.31 and bGPSy < -4.26) or (bGPSx > 55.90 and bGPSx < 55.95 and bGPSy > -4.31 and bGPSy < -4.155)"
sqlC = "update bike_info set barea = 'C' where (bGPSx > 55.88 and bGPSx < 55.95 and bGPSy > -4.15 and bGPSy < -4.0) or (bGPSx > 55.90 and bGPSx < 55.95 and bGPSy > -4.155 and bGPSy < -4.0)"
sqlD = "update bike_info set barea = 'D' where (bGPSx > 55.81 and bGPSx < 55.88 and bGPSy > -4.31 and bGPSy < -4.26) or (bGPSx > 55.81 and bGPSx < 55.85 and bGPSy > -4.31 and bGPSy < -4.155)"
sqlE = "update bike_info set barea = 'E' where (bGPSx > 55.81 and bGPSx < 55.88 and bGPSy > -4.15 and bGPSy < -4.0) or (bGPSx > 55.81 and bGPSx < 55.85 and bGPSy > -4.155 and bGPSy < -4.0)"

cur.execute(sqlA)
cur.execute(sqlB)
cur.execute(sqlC)
cur.execute(sqlD)
cur.execute(sqlE)
#commit
conn.commit()
cur.close()
conn.close()


# update the area information for customer

# Connect to the database
conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor()

sqlA = "update customer_info set uarea = 'A' where (uGPSx > 55.85 and uGPSx < 55.90) and (uGPSy > -4.26 and uGPSy < -4.15)"
sqlB = "update customer_info set uarea = 'B' where (uGPSx > 55.88 and uGPSx < 55.95 and uGPSy > -4.31 and uGPSy < -4.26) or (uGPSx > 55.90 and uGPSx < 55.95 and uGPSy > -4.31 and uGPSy < -4.155)"
sqlC = "update customer_info set uarea = 'C' where (uGPSx > 55.88 and uGPSx < 55.95 and uGPSy > -4.15 and uGPSy < -4.0) or (uGPSx > 55.90 and uGPSx < 55.95 and uGPSy > -4.155 and uGPSy < -4.0)"
sqlD = "update customer_info set uarea = 'D' where (uGPSx > 55.81 and uGPSx < 55.88 and uGPSy > -4.31 and uGPSy < -4.26) or (uGPSx > 55.81 and uGPSx < 55.85 and uGPSy > -4.31 and uGPSy < -4.155)"
sqlE = "update customer_info set uarea = 'E' where (uGPSx > 55.81 and uGPSx < 55.88 and uGPSy > -4.15 and uGPSy < -4.0) or (uGPSx > 55.81 and uGPSx < 55.85 and uGPSy > -4.155 and uGPSy < -4.0)"

cur.execute(sqlA)
cur.execute(sqlB)
cur.execute(sqlC)
cur.execute(sqlD)
cur.execute(sqlE)

conn.commit()
cur.close()
conn.close()

