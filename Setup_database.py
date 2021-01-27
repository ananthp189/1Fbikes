# Database

# 1. Customer information:
# ID                 integer  PRIMARY KEY
# UserName   text
# Password    text
# rent_times
# Balance
# starttime
# endtime

# 2. Bike information:
# bike_ID       integer  PRIMARY KEY
# x_axis        (in order to show the geographic position of the bike)
# y_axis
# Lifetime
# Technical Information
# reserve information


import random as r
import pymysql 


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
conn = pymysql.connect(user='root', password='test1234', host='127.0.0.1', database='test2')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS customer_info(
    ID integer PRIMARY KEY,
    UserName text,
    Password text,
    rent_times text,
    Balance text,
    starttime text,
    endtime text);""")


# Insert the data:
for i in range(len(name)):            # import 100 customer information
  pw = r.choice(passwd)
  rt = str(r.randint(0, 100))
  balance = str(r.randint(0, 100))
  cur.execute("insert into customer_info(ID, UserName, Password, rent_times, Balance) values(%s,%s,%s,%s,%s)",(i+1,name[i],pw, rt, balance))

cur.execute('select * from customer_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()





############################ Bike Information Database ############################

# Connect to the database
conn = pymysql.connect(user='root', password='test1234', host='127.0.0.1', database='test2')
cur = conn.cursor() 
cur.execute("""CREATE TABLE IF NOT EXISTS bike_info(
    bike_ID integer PRIMARY KEY,
    x_axis text,
    y_axis text,
    Lifetime text,
    Technical_info text,
    Reserve_info text);""")


# Insert the data:
for i in range(500):        # import 500 bikes information
  x = str(r.randint(0, 100))
  y = str(r.randint(0, 100))
  lt = str(r.randint(0, 5))
  T_info = str(r.randint(0, 1))           # 0 means no technical issues, 1 means have technical issues.
  R_info = str(r.randint(0, 1))           # 0 means not been reserved, 1 means is reserved by some people.
  cur.execute("insert into bike_info(bike_ID, x_axis, y_axis, Lifetime, Technical_info, Reserve_info) values(%s,%s,%s,%s,%s,%s)",(i+1, x, y, lt, T_info, R_info))

cur.execute('select * from bike_info')
for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()
