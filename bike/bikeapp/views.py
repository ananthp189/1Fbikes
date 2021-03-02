import json
import math
import time
import datetime
from pyecharts.charts import Pie, WordCloud
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode
import folium
from folium.plugins import HeatMap
from pyecharts.faker import Faker
import pandas as pd
import random

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymysql
import pymysql.cursors
from django.contrib import messages
import os
from django.http import StreamingHttpResponse
from django.conf import settings
import urllib.parse



# login webpage
def login(request):
    return render(request,'bikeapp/login.html')

# register page
def register(request):
    return render(request,'bikeapp/register.html')

# main page for customers login
def main(request):
    return render(request,'bikeapp/index.html')

# data visualization page
def dataVis (request) :
    return render(request, 'bikeapp/datavisualization.html')

# login function save method
def save(request):
    has_register = 0#Used to record whether the current account already exists, 0: does not exist 1: already exists
    a = request.GET#Get get() request
    #print(a)
    #Get the data submitted in the previous paragraph through get() request
    userID = a.get('UserID')
    name = a.get('Name')
    password = a.get('Password')
    telephone = a.get('Telephone')
    bankcard = a.get('Bankcard')
    ux = random.uniform(55.85, 55.90)
    uy = random.uniform(-4.15, -4.26)
    uxx = round(ux, 10)
    uyy = round(uy, 10)
    uarea = "A"
    utype = 0
    totaltime = 0

    #print(userName,passWord)
    #connect database
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    #create cursor
    cursor = db.cursor()
    #SQL sentence
    sql1 = 'select * from customer_info'
    #Execute SQL sentence
    cursor.execute(sql1)
    #Query all data stored in all_users
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userID in all_users[i]:
            #Indicates that the account already exists
            has_register = 1

        i += 1
    if has_register == 0:
        # Insert the username and password into the database
        sql2 = 'insert into customer_info(ID,UserName,Password,renttime,usertype,uGPSx,uGPSy,uarea,Tel,Bankcard) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql2, (userID, name, password, totaltime, utype, uxx, uyy, uarea, telephone, bankcard))
        db.commit()
        # When you need to modify the statement in the database, add, delete, modify..., plus commit
        cursor.close()
        db.close()
        # tkinter.messagebox.showerror("Prompt", "Congratulations, the registered user is successful!")
        # return HttpResponse('register sucess')
        return render(request, 'bikeapp/register_succeed.html', {'has_register':has_register, 'userName': name})

    # else:
    if has_register == 1:
        cursor.close()
        db.close()
        # tkinter.messagebox.showerror("Prompt","Sorry, the user name is duplicate, registration failed")
        # return HttpResponse('user exist!')
        return render(request, 'bikeapp/register_succeed.html', {'has_register':has_register, 'userName': name})

# Login function query method
def query(request):
    a = request.GET
    userid = a.get('userID')
    password = a.get('password')
    user_tup = (userid, password)
    global ID
    ID = userid
    # Define global variables! ! ! ! ! ! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()

    # Get operation cursor
    sql = 'select ID,Password from customer_info'
    cursor.execute(sql)
    # Execute sql statement
    all_users = cursor.fetchall()
    # All query results are returned
    cursor.close()
    # Close cursor
    db.close()
    # close database
    has_user = 0
    i = 0
    while i < len(all_users):
        # print("!!!!!!!!!!!!!!!!!!!!!!")
        # print(all_users[i])
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
        # print("############################")
        # print(has_user)
    if has_user == 1:
        # Query the name of the user account
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor2 = db.cursor(pymysql.cursors.DictCursor)
        sql1 = 'select UserName from customer_info where ID ="{}"'
        sql2 = sql1.format(userid)
        cursor2.execute(sql2)
        username = cursor2.fetchall()
        # Define global variables! ! ! ! ! ! !!!!!!!!
        global username1
        username1 = username
        sql3 = 'select usertype from customer_info where ID ="{}"'
        sql4 = sql3.format(userid)
        cursor2.execute(sql4)
        utype = cursor2.fetchall()
        cursor2.close()
        db.close()
        usertype = utype[0]["usertype"]
        if usertype == '1':
            return render(request, 'bikeapp/operatormain.html', {'has_user': has_user, 'userName': username})
        elif usertype == '2':
            return render(request, 'bikeapp/managermain.html', {'has_user': has_user, 'userName': username})
        else:
            return render(request, 'bikeapp/index.html', {'has_user': has_user, 'userName': username})





     # return HttpResponse('login success')
    else:
        return render(request, 'bikeapp/login.html', {'has_user': has_user})
        # return HttpResponse('password or username wrong!')


def defective(request):
    return render(request,'bikeapp/defective.html')

def dd(request):
    has_report = 0
    d = request.GET
    bikeid = d.get('BikeID')
    bikeproblem = d.get('Bikeproblem')

    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    sql1 = 'select * from bike_info'
    cursor.execute(sql1)
    all_bike = cursor.fetchall()
    i = 0
    while i < len(all_bike):
        if bikeid in all_bike[i]:
            has_report = 1

        i += 1
    if has_report == 1:
        usage = 0  # set bike_usage = 0 (don't use)
        status = 1  # set bike status = 1 (0 good, 1 broken)
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor = db.cursor()
        sql = 'UPDATE bike_info SET bproblem=%s, busage=%s, bstatus=%s where bID=%s'
        cursor.execute(sql, (bikeproblem, usage, status, bikeid))
        db.commit()
        cursor.close()
        db.close()

    return render(request,'bikeapp/defective.html',{'has_report': has_report})



# payment
def payment(request):
    return render(request,'bikeapp/pay.html')


def pay(request):
    # creat paymentid
    bID = BID # get from rentbike function set a global various
    #payid = random.sample(range(10002,91000),1)
    payid = PID # get from rentbike function set a global various
    # set payment status
    status = 0
    # duration
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor2 = db.cursor(pymysql.cursors.DictCursor)
    sql1 = 'select renttime from customer_info where ID ="{}"'
    sql2 = sql1.format(ID)
    cursor2.execute(sql2)
    totaltime = cursor2.fetchall()
    # totaltime = 612  # get from user function set a global various

    #get start time
    cursor5 = db.cursor(pymysql.cursors.DictCursor)
    sql1 = 'select starttime from pay_info where pID ="{}"'
    sql2 = sql1.format(payid)
    cursor5.execute(sql2)
    startt = cursor5.fetchall()
    starttime = datetime.datetime.strptime(startt[0]["starttime"], "%Y-%m-%d %H:%M:%S")
    #get end time
    sql3 = 'select endtime from pay_info where pID ="{}"'
    sql4 = sql3.format(payid)
    cursor5.execute(sql4)
    endt = cursor5.fetchall()
    # print("!!!!!", endt)
    endtime = datetime.datetime.strptime(endt[0]["endtime"], "%Y-%m-%d %H:%M:%S")
    print("!!!!!", endtime)
    cursor5.close()
    db.close()

    # computed duration time
    bduration = endtime - starttime
    # count = bduration // 100 # get the hour
    original_bill = bduration * 0.01  # 0.01 pounds a minute
    if totaltime >= 500:
        discount_bill = original_bill * 0.8 # discount, 80% off
    else:
        discount_bill = original_bill # no discount

#   #inupt duration, original bill, discount bill
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    sql5 = 'UPDATE pay_info SET duration=%s, oribill=%s, discount=%s  where pID=%s'
    cursor.execute(sql5, (bduration, original_bill, discount_bill, payid))
    db.commit()
    cursor.close()
    db.close()

    #button return
    #<button class="" type="submit" name="subtype" value="1"> payment</button> in html
    p = request.GET
    submit1 = p.get('subtype')
    if submit1 == 1:
        put = 1 # return various
        status = 1  # pay successful
        buse = 0  # in bike chart
        totaltime = totaltime + bduration
    # database

    #update payment status
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    sql3 = 'UPDATE pay_info SET pstatus=%s where pID=%s'
    cursor.execute(sql3, (status, payid))
    db.commit()

    #update user status
    sql3 = 'UPDATE customer_info SET renttime=%s where ID=%s'
    cursor.execute(sql3, (totaltime, ID))
    db.commit()

    # update  bike status
    sql4 = 'UPDATE bike_info SET busage=%s where bID=%s'
    cursor.execute(sql4, (buse, bID))
    db.commit()
    cursor.close()
    db.close()

    return render(request,'bikeapp/pay.html', {'payid': payid, 'time': bduration, 'original_bill': original_bill, 'discount_bill': discount_bill, 'put':put })

#show bike map-- Front and back interaction
def bikemap(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    #search bike information to show to managers.
    sql = 'select bID,bstatus,  barea, bpassword, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    #select gpsx and gpsy for drawing in the map
    sqlGPS = 'select bGPSx,bGPSy from bike_info'
    cursor.execute(sqlGPS)
    bikesGPS = cursor.fetchall()
    #close cursor
    cursor.close()
    # close database
    db.close()

    allbikes_list = []
    for i in range(len(all_bikes)):
        #list() to replace dict.value to list
        allbikes_list.append(list(all_bikes[i].values()))

    print(allbikes_list)
    bGPS = []
    for i in range(len(bikesGPS)):
        bGPS.append(list(bikesGPS[i].values()))
    for i in range(len(bGPS)):
        for j in range(2):
            bGPS[i][j] = (bGPS[i][j])
    print("_-_")
    print(bGPS)
    #
    return render(request,'bikeapp/bike_map.html', {'bikeGPS': json.dumps(bGPS), 'bikesinfo': json.dumps(allbikes_list)})





#---------------Track bikes module  ----------------------#

def locationmap(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # search bike information to show to managers.
    sql = 'select bID,bstatus,  barea, bpassword, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    # select gpsx and gpsy for drawing in the map
    sqlGPS = 'select bGPSx,bGPSy from bike_info'
    cursor.execute(sqlGPS)
    bikesGPS = cursor.fetchall()
    # Close cursor
    cursor.close()
    #close database
    db.close()

    allbikes_list = []
    for i in range(len(all_bikes)):
        # list() to replace dict.value to list
        allbikes_list.append(list(all_bikes[i].values()))

    print(allbikes_list)
    bGPS = []
    for i in range(len(bikesGPS)):
        bGPS.append(list(bikesGPS[i].values()))
    for i in range(len(bGPS)):
        for j in range(2):
            bGPS[i][j] = (bGPS[i][j])
    print("_-_")
    print(bGPS)

    #---------------add table - ---------------------
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = 'select bID, bstatus, barea,bpassword, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    cursor.close()
    # Close database
    db.close()
    #
    return render(request, 'bikeapp/locationmap.html'),

#--------------- Rent Bike Module  ----------------------#

def rent(request):

    #Setup database connection
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    #Get user from global id
    cursor.execute("SELECT * FROM customer_info WHERE ID = %s", ID)
    user = cursor.fetchone()

    # fetch all bikes
    # calculate all the distances between user and bikes
    # choose the bike with the minimum distance

    cursor.execute("SELECT * FROM bike_info WHERE busage = 0 AND bstatus = 0")

    bikes = cursor.fetchall()
    mindistance = None
    bike = None

    # for every bike calculate the distance between user and bike
    # if the minimum distance is none or less than distance
    # set the mindistance to distance
    # set bike to availablebike

    for availableBike in bikes:
        distancex = pow((float(user["uGPSx"])-float(availableBike["bGPSx"])),2)
        distancey = pow((float(user["uGPSy"]) - float(availableBike["bGPSy"])), 2)
        distance = math.sqrt(distancex + distancey)
        if not isinstance(mindistance, float) or distance < mindistance:
            mindistance = distance
            bike = availableBike
    

    print(bike)
    
    if bike is None or bikes is None:
        error="no bikes available"
        return render(request, 'bikeapp/rentbike.html', {'bikeid': error})        
    cursor.execute("UPDATE bike_info SET busage = 1 WHERE bID = %s", int(bike["bID"]))
    db.commit()


    # with global id get user
    # assign bike based on user area
    # record start time
    global PID
    PID = random.sample(range(10002, 91000), 1) 
    sql2 = "INSERT INTO pay_info (pID, ID, bID, starttime,endtime,duration,oribill,discount,startGPSx, startGPSy,endGPSx,endGPSy,pstatus) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql2, (PID, user["ID"], bike["bID"], datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S" ),datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S" ),0,0,0, bike["bGPSx"], bike["bGPSy"], bike["bGPSx"], bike["bGPSy",0]))
    db.commit()
    bikeid = bike["bID"]
    bikepin = bike["bpassword"]
    global BID
    BID = bike["bID"]
   
    return render(request, 'bikeapp/rentbike.html', {'bike_id': bikeid,'bike_pin': bikepin})

#--------------- Return Bike Module  ----------------------#

#return a bike function

# return bike after renting and using the bike

def returnBike(request):
    # Setup database connection
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor(pymysql.cursors.DictCursor)


    #Get user from global id
    cursor.execute("SELECT * FROM customer_info WHERE ID = %s", ID)
    user = cursor.fetchone()
    #Get bikeinfo from glbal PID
    cursor.execute("SELECT * FROM bike_info WHERE bID = %s", int(BID))
    bike = cursor.fetchone()

    # set the fetched bike to returned status and update its new gps
    cursor.execute("UPDATE bike_info SET busage = 0 , bGPSx=%s , bGPSy=%s WHERE bID = %s",(user["uGPSx"], user["uGPSy"], int(BID)))
    db.commit()
    # return bike based on user current location
    # record end time and update the table
    sql1 = "update pay_info SET  endtime=%s, endGPSx=%s, endGPSy=%s where  pID= %s"
    cursor.execute(sql1,(datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S" ), user["uGPSx"], user["uGPSy"], PID))
    db.commit()
    cursor.execute("SELECT * FROM pay_info WHERE pID = %s",PID)
    bduration=0
    payinfo=None
    payinfo=cursor.fetchone()
    if payinfo is not None:
        bduration = (float(payinfo["endtime"])) - (float(payinfo["starttime"]))
    db.commit()
    bikeid = BID
    return render(request, 'bikeapp/returnbike.html',{'bike_id': bikeid},{'duration': bduration})  ,

#-------------movebike------------

###########movebike-collect data########
def movebike(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = 'select bID, bstatus, bGPSx,bGPSy, barea, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    # 查询结果全部返回
    ###################li------add-----------
    area_list = []
    for a in all_bikes:
        area_list.append(a['barea'])
    a=area_list.count("A")
    b=area_list.count("B")
    c=area_list.count("C")
    d=area_list.count("D")
    e=area_list.count("E")
    count_list=[a,b,c,d,e]
    print(count_list)
    result = dict()
    for b in set(area_list):
        result[b] = area_list.count(b)
    print(result.items())
    #假设每个区域标准80辆车，显示车辆不足区域
    normal = 80;
    warn_list = []
    for i in result.items():
        if i[1] < normal:
            y = "area " + i[0] + " needs more bikes!Please adjust the distribution of bicycles "
            print(y)
            warn_list.append(y)
    if len(warn_list)==0:
        k = "Every area is good"
        warn_list.append(k)
    #print(warn_list)
    ######################
    cursor.close()
    # 关闭游标
    db.close()
    # 关闭数据库
    # print(all_bikes)
    return render(request, 'bikeapp/movebike.html',{'allbikes': all_bikes, 'result': result.items(),'warn':warn_list,'count':count_list})



#----------------select-------------------
def select(request):
    a = request.POST
    #b = request.REQUEST.get
    select_move_bid = request.POST.getlist('select_bid')
    print("看这里！！！", select_move_bid)
    select_move_area = a.get('select_barea')
    print(select_move_area)
    all_area = ["A","B","C","D","E"]
    if select_move_area in all_area:
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor = db.cursor()
        for i in select_move_bid:
            #随机生成gps
            global gpsx, gpsy
            if select_move_area == 'A':
                gpsx = random.uniform(55.85,55.90)
                gpsy = random.uniform(-4.15,-4.26)
            elif select_move_area == 'B':
                print("aaaaaaaaaa")
                gpsx = random.uniform(55.90,55.95)
                gpsy = random.uniform(-4.16,-4.31)
            elif select_move_area == 'C':
                gpsx = random.uniform(55.90,55.95)
                gpsy = random.uniform(-4.0,-4.16)
            elif select_move_area == 'D':
                gpsx = random.uniform(55.81,55.85)
                gpsy = random.uniform(-4.16,-4.31)
            elif select_move_area == 'E':
                gpsx = random.uniform(55.81,55.85)
                gpsy = random.uniform(-4.0,-4.16)
            gpsx = str(gpsx)
            gpsy = str(gpsy)
            print("GPS！！", gpsx)
            sql = 'update bike_info set barea=%s, bGPSx=%s,bGPSy=%s where bID=%s'
            cursor.execute(sql, (select_move_area, gpsx, gpsy, i))
        db.commit()
        cursor.close()
        db.close()
        #return HttpResponse('Succeed',select_move_bid)
        #messages.success(request, "Succeed!!")
        #return HttpResponse('messages.success(request, "Succeed!!")', select_move_bid)
        # return render(request,'bikeapp/movebike.html',{'message':messages.success(request, "Succeed!!")})
        messages.success(request, "Succeed!!")
        return HttpResponseRedirect('http://127.0.0.1:8000/movebike/')
        #return messages
    else:
        messages.success(request, "Incorrect input, please check!!")
        return HttpResponseRedirect('http://127.0.0.1:8000/movebike/')



#---------------repair bake-------------
def repairmap(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # search bike information to show to managers.
    sql = 'select bID,bstatus,  barea, bpassword, busage,bproblem from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    # select gpsx and gpsy for drawing in the map
    sqlGPS = 'select bGPSx,bGPSy from bike_info'
    cursor.execute(sqlGPS)
    bikesGPS = cursor.fetchall()
    cursor.close()
    # 关闭游标
    db.close()
    # 关闭数据库
    print(all_bikes)
    #显示坏自行车
    allbikes_list = []
    badbikes_list=[]
    for i in range(len(all_bikes)):
    #     # list() to replace dict.value to list
         if all_bikes[i]['bstatus'] == '1':
            allbikes_list.append(list(all_bikes[i].values()))
            badbikes_list.append(all_bikes[i])
    #统计坏自行车数量 提示给操纵员
    num = str(len(badbikes_list))
    print(num)
    #########################
    bGPS = []
    for i in range(len(bikesGPS)):
        bGPS.append(list(bikesGPS[i].values()))
    for i in range(len(bGPS)):
        for j in range(2):
            bGPS[i][j] = (bGPS[i][j])
    print("_-_")
    print(bGPS)
    return render(request, 'bikeapp/repairbike.html',
                  {'bikeGPS': json.dumps(bGPS), 'bikesinfo': json.dumps(allbikes_list), 'allbikes': all_bikes,'repair':badbikes_list,'number':num})
def repair(request):
    a = request.POST
    select_repair_bid = request.POST.getlist('select_bid')
    #repair_bid = a.get('bid')
    #rapair_status = a.get('bstatus')
    if len(select_repair_bid) != 0:
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor = db.cursor()
        sql = 'update bike_info set bstatus=0,bproblem=null where bID=%s'
        cursor.execute(sql, (select_repair_bid))
        db.commit()
        cursor.close()
        db.close()
        #return HttpResponse('repaired--succeed')
        messages.success(request, "Succeed!!")
        return HttpResponseRedirect('http://127.0.0.1:8000/repairbike/')
        # return messages
    else:
        messages.success(request, "Incorrect input, please check!!")
        return HttpResponseRedirect('http://127.0.0.1:8000/repairbike/')
#-----------------location bike------------------f
# def locationbike(request):
#     db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
#     # add “pymysql.cursors.DictCursor” to pass variables to web-front
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     sql = 'select bID, bstatus, barea,bpassword, busage from bike_info'
#     cursor.execute(sql)
#     all_bikes = cursor.fetchall()
#     cursor.close()
#      # 关闭游标
#     db.close()
#      #关闭数据库
#     print(all_bikes)
#     return render(request, 'bikeapp/locationmap.html', {'allbikes': all_bikes})
#-----------------------location bike----------------------------
#show all bikes
def locationmap(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # search bike information to show to managers.
    sql = 'select bID,bstatus,  barea, bpassword, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    # select gpsx and gpsy for drawing in the map
    sqlGPS = 'select bGPSx,bGPSy from bike_info'
    cursor.execute(sqlGPS)
    bikesGPS = cursor.fetchall()
    cursor.close()
    # 关闭游标
    db.close()
    # 关闭数据库
    allbikes_list = []
    for i in range(len(all_bikes)):
        # list() to replace dict.value to list
        allbikes_list.append(list(all_bikes[i].values()))

    print(allbikes_list)
    bGPS = []
    for i in range(len(bikesGPS)):
        bGPS.append(list(bikesGPS[i].values()))
    for i in range(len(bGPS)):
        for j in range(2):
            bGPS[i][j] = (bGPS[i][j])
    print("_-_")
    print(bGPS)
    #---------------add table----------------------
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = 'select bID, bstatus, barea,bpassword, busage from bike_info'
    cursor.execute(sql)
    all_bikes = cursor.fetchall()
    cursor.close()
    # 关闭游标
    db.close()
    #
    return render(request, 'bikeapp/locationmap.html',
                  {'bikeGPS': json.dumps(bGPS), 'bikesinfo': json.dumps(allbikes_list),'allbikes': all_bikes})


##### Data Visualizasion ######
def pie_User_Structure():

    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    cur.execute('select * from customer_info\
                where usertype = %s', ("0"))

    num_normal = len(cur.fetchall())
    conn.commit()

    cur.execute('select * from customer_info\
                where usertype = %s', ("1"))

    num_prime = len(cur.fetchall())
    conn.commit()

    cur.execute('select * from customer_info\
                where usertype = %s', ("2"))

    num_operater = len(cur.fetchall())
    conn.commit()

    cur.execute('select * from customer_info\
                where usertype = %s', ("3"))

    num_manager = len(cur.fetchall())
    conn.commit()

    cur.close()
    conn.close()

    Position = ("Prime customer", "Normal customer", "Operater", "Manager")
    Num = (num_prime, num_normal, num_operater, num_manager)

    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(Position, Num)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="User Structure"))
        .render("templates/bikeapp/pie_User_Structure.html")
    )


def pie_bike_status():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("A", "0"))

    num_A0 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("A", "1"))

    num_A1 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("B", "0"))

    num_B0 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("B", "1"))

    num_B1 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("C", "0"))

    num_C0 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("C", "1"))

    num_C1 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("D", "0"))

    num_D0 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("D", "1"))

    num_D1 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("E", "0"))

    num_E0 = len(cur.fetchall())

    cur.execute('select * from bike_info\
                where barea = %s and bstatus = %s', ("E", "1"))

    num_E1 = len(cur.fetchall())

    inner_x_data = ["A", "B", "C", "D", "E"]
    inner_y_data = [num_A0 + num_A1, num_B0 + num_B1, num_C0 + num_C1, num_D0 + num_D1, num_E0 + num_E1]
    inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

    outer_x_data = ["A_good", "A_broken", "B_good", "B_broken", "C_good", "C_broken", "D_good", "D_broken", "E_good",
                    "E_broken"]
    outer_y_data = [num_A0, num_A1, num_B0, num_B1, num_C0, num_C1, num_D0, num_D1, num_E0, num_E1]
    outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

    (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="Area",
            data_pair=inner_data_pair,
            radius=[0, "30%"],
            label_opts=opts.LabelOpts(position="inner"),
        )
            .add(
            series_name="status",
            radius=["40%", "55%"],
            data_pair=outer_data_pair,
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            )
        )
        .render("templates/bikeapp/pie_bike_status.html")
    )


def bar_rent_duration():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    sql = 'select * from customer_info'
    cur.execute(sql.encode('utf-8'))
    var_name = cur.description
    name = []
    for i in range(len(var_name)):
        name.append(var_name[i][0])
    datalist = []
    var_data = cur.fetchall()
    for i in range(len(var_data)):
        datalist.append(var_data[i])
    file_test = pd.DataFrame(columns=name, data=datalist)
    file_test.to_csv("customer_info_DV.csv")

    sql = 'select * from pay_info'
    cur.execute(sql.encode('utf-8'))
    var_name = cur.description
    name = []
    for i in range(len(var_name)):
        name.append(var_name[i][0])
    datalist = []
    var_data = cur.fetchall()
    for i in range(len(var_data)):
        datalist.append(var_data[i])
    file_test = pd.DataFrame(columns=name, data=datalist)
    file_test.to_csv("pay_info_DV.csv")

    pay_info = pd.read_csv("pay_info_DV.csv", index_col=0)
    customer_info = pd.read_csv("customer_info_DV.csv", index_col=0)

    # merge two dataframe
    combined_info = pd.merge(pay_info, customer_info)
    # normal customer duration
    nh_1 = ((combined_info["duration"] <= 60) & (combined_info["usertype"] == 0)).sum()
    nh_2 = ((combined_info["duration"] > 60) & (combined_info["duration"] <= 120) & (
                combined_info["usertype"] == 0)).sum()
    nh_3 = ((combined_info["duration"] > 120) & (combined_info["duration"] <= 180) & (
                combined_info["usertype"] == 0)).sum()
    nh_4 = ((combined_info["duration"] > 180) & (combined_info["duration"] <= 240) & (
                combined_info["usertype"] == 0)).sum()
    nh_5 = ((combined_info["duration"] > 240) & (combined_info["duration"] <= 300) & (
                combined_info["usertype"] == 0)).sum()
    nh_6 = ((combined_info["duration"] > 300) & (combined_info["duration"] <= 900) & (
                combined_info["usertype"] == 0)).sum()
    # prime customer duration
    ph_1 = ((combined_info["duration"] <= 60) & (combined_info["usertype"] == 1)).sum()
    ph_2 = ((combined_info["duration"] > 60) & (combined_info["duration"] <= 120) & (
                combined_info["usertype"] == 1)).sum()
    ph_3 = ((combined_info["duration"] > 120) & (combined_info["duration"] <= 180) & (
                combined_info["usertype"] == 1)).sum()
    ph_4 = ((combined_info["duration"] > 180) & (combined_info["duration"] <= 240) & (
                combined_info["usertype"] == 1)).sum()
    ph_5 = ((combined_info["duration"] > 240) & (combined_info["duration"] <= 300) & (
                combined_info["usertype"] == 1)).sum()
    ph_6 = ((combined_info["duration"] > 300) & (combined_info["duration"] <= 900) & (
                combined_info["usertype"] == 1)).sum()

    x_label = ("Under 1 hour", "1~2 hours", "2~3 hours", "3~4 hours", "4~5 hours", "Above 5 hours")

    c = (
        Bar()
            .add_xaxis(x_label)
            .add_yaxis("Normal Customer", [int(nh_1), int(nh_2), int(nh_3), int(nh_4), int(nh_5), int(nh_6)])
            .add_yaxis("Prime Customer", [int(ph_1), int(ph_2), int(ph_3), int(ph_4), int(ph_5), int(ph_6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Rent Duration", subtitle="Normal & Prime"))
            .render("templates/bikeapp/bar_rent_duration.html")
    )


def liquid():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    sql = 'select * from bike_info'
    cur.execute(sql.encode('utf-8'))
    var_name = cur.description
    name = []
    for i in range(len(var_name)):
        name.append(var_name[i][0])
    datalist = []
    var_data = cur.fetchall()
    for i in range(len(var_data)):
        datalist.append(var_data[i])
    file_test = pd.DataFrame(columns=name, data=datalist)
    file_test.to_csv("bike_info_DV.csv")

    bike_info = pd.read_csv("bike_info_DV.csv", index_col=0)  # input datatable

    bike_usage_num = (bike_info["busage"] == 1).sum()  # count how many bike is being used
    bike_usage_rate = bike_usage_num / 500  # usage rate

    customer_info = pd.read_csv("customer_info_DV.csv", index_col=0)  # input datatable

    customer_prime_num = (customer_info["usertype"] == 1).sum()
    customer_total_num = (customer_info["usertype"] == 0).sum() + customer_prime_num
    customer_prime_rate = customer_prime_num / customer_total_num

    l1 = (
        Liquid()
            .add("Bike ueage Rate", [bike_usage_rate, bike_usage_num], center=["60%", "50%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="Liquid Chart"))
    )

    l2 = Liquid().add(
        "Prime Rate",
        [customer_prime_rate],
        center=["25%", "50%"],
        label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )

    grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
    grid.render("templates/bikeapp/liquid.html")


def heatmap_bike():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    sql = 'select * from bike_info'
    cur.execute(sql.encode('utf-8'))
    var_name = cur.description
    name = []
    for i in range(len(var_name)):
        name.append(var_name[i][0])
    datalist = []
    var_data = cur.fetchall()
    for i in range(len(var_data)):
        datalist.append(var_data[i])
    file_test = pd.DataFrame(columns=name, data=datalist)
    file_test.to_csv("bike_info_DV.csv")

    # define the glasgow map
    gla = folium.Map(location=[55.85, -4.235], zoom_start=12)

    # add area A
    area_A = [
        [55.90, -4.26],
        [55.90, -4.15],
        [55.85, -4.15],
        [55.85, -4.26]
    ]
    gla.add_child(folium.Polygon(
        locations=area_A,
        weight=3,
        color="yellow"
    ))

    # add area B
    area_B = [
        [55.95, -4.31],
        [55.88, -4.31],
        [55.88, -4.26],
        [55.90, -4.26],
        [55.90, -4.155],
        [55.95, -4.155]
    ]
    gla.add_child(folium.Polygon(
        locations=area_B,
        weight=3,
        color="blue"
    ))

    # add area C
    area_C = [
        [55.95, -4.155],
        [55.90, -4.155],
        [55.90, -4.15],
        [55.88, -4.15],
        [55.88, -4.0],
        [55.95, -4.0]
    ]
    gla.add_child(folium.Polygon(
        locations=area_C,
        weight=3,
        color="green"
    ))

    # add area D
    area_D = [
        [55.88, -4.31],
        [55.81, -4.31],
        [55.81, -4.155],
        [55.85, -4.155],
        [55.85, -4.26],
        [55.88, -4.26]
    ]
    gla.add_child(folium.Polygon(
        locations=area_D,
        weight=3,
        color="red"
    ))

    # add area E
    area_E = [
        [55.85, -4.155],
        [55.81, -4.155],
        [55.81, -4.0],
        [55.88, -4.0],
        [55.88, -4.15],
        [55.85, -4.15]
    ]

    gla.add_child(folium.Polygon(
        locations=area_E,
        weight=3,
        color="orange"
    ))
    # get data from database
    bike_info = pd.read_csv("bike_info_DV.csv", index_col=0)
    x = bike_info["bGPSx"]
    y = bike_info["bGPSy"]
    # merge together
    data = list(zip(x, y))
    # print heatmap for bike
    gla.add_child(HeatMap(data=data[5:]))
    # save html file
    gla.save("templates/bikeapp/heatmap_bike.html")


def heatmap_payment():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    sql = 'select * from pay_info'
    cur.execute(sql.encode('utf-8'))
    var_name = cur.description
    name = []
    for i in range(len(var_name)):
        name.append(var_name[i][0])
    datalist = []
    var_data = cur.fetchall()
    for i in range(len(var_data)):
        datalist.append(var_data[i])
    file_test = pd.DataFrame(columns=name, data=datalist)
    file_test.to_csv("pay_info_DV.csv")

    # define the glasgow map
    gla = folium.Map(location=[55.85, -4.235], zoom_start=12)
    # add area A
    area_A = [
        [55.90, -4.26],
        [55.90, -4.15],
        [55.85, -4.15],
        [55.85, -4.26]
    ]
    gla.add_child(folium.Polygon(
        locations=area_A,
        weight=3,
        color="yellow"
    ))
    # add area B
    area_B = [
        [55.95, -4.31],
        [55.88, -4.31],
        [55.88, -4.26],
        [55.90, -4.26],
        [55.90, -4.155],
        [55.95, -4.155]
    ]
    gla.add_child(folium.Polygon(
        locations=area_B,
        weight=3,
        color="blue"
    ))
    # add area C
    area_C = [
        [55.95, -4.155],
        [55.90, -4.155],
        [55.90, -4.15],
        [55.88, -4.15],
        [55.88, -4.0],
        [55.95, -4.0]
    ]
    gla.add_child(folium.Polygon(
        locations=area_C,
        weight=3,
        color="green"
    ))
    # add area D
    area_D = [
        [55.88, -4.31],
        [55.81, -4.31],
        [55.81, -4.155],
        [55.85, -4.155],
        [55.85, -4.26],
        [55.88, -4.26]
    ]
    gla.add_child(folium.Polygon(
        locations=area_D,
        weight=3,
        color="red"
    ))
    # add area E
    area_E = [
        [55.85, -4.155],
        [55.81, -4.155],
        [55.81, -4.0],
        [55.88, -4.0],
        [55.88, -4.15],
        [55.85, -4.15]
    ]
    gla.add_child(folium.Polygon(
        locations=area_E,
        weight=3,
        color="orange"
    ))
    # get data from database
    pay_info = pd.read_csv("pay_info_DV.csv", index_col=0)
    x = pay_info["startGPSx"]
    y = pay_info["startGPSy"]
    # merge together
    data = list(zip(x, y))
    # print heatmap for bike
    gla.add_child(HeatMap(data=data[2:]))
    # save html file
    gla.save("templates/bikeapp/heatmap_payment.html")


def bar_datazoom_Monthly_payment_quantity():
    conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
    cur = conn.cursor()

    x = []
    # Jan-Nov
    for i in range(1, 12):
        day1 = datetime.datetime(2020, i, 1).strftime('%Y-%m-%d %H:%M:%S')
        day2 = datetime.datetime(2020, i + 1, 1).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("select * from pay_info where starttime >= %s and starttime < %s", (day1, day2))
        x.append(len(cur.fetchall()))
    # Dec
    day1 = datetime.datetime(2020, 12, 1).strftime('%Y-%m-%d %H:%M:%S')
    day2 = datetime.datetime(2020, 12, 31).strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("select * from pay_info where starttime >= %s and starttime < %s", (day1, day2))
    x.append(len(cur.fetchall()))
    # Jan-Mar
    for i in range(1, 3):
        day1 = datetime.datetime(2021, i, 1).strftime('%Y-%m-%d %H:%M:%S')
        day2 = datetime.datetime(2021, i + 1, 1).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("select * from pay_info where starttime >= %s and starttime < %s", (day1, day2))
        x.append(len(cur.fetchall()))

    day1 = datetime.datetime(2021, 3, 1).strftime('%Y-%m-%d %H:%M:%S')
    day2 = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("select * from pay_info where starttime >= %s and starttime < %s", (day1, day2))
    x.append(len(cur.fetchall()))

    x_label = []
    for i in range(14):
        x_label.append("Month" + str(i + 1))

    c = (
        Bar()
            .add_xaxis(x_label)
            .add_yaxis("Payment amount", x, color=Faker.rand_color())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Monthly payment quantity- DataZoom）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
        .render("templates/bikeapp/bar_datazoom_Monthly_payment_quantity.html")
    )


def dv_bstatus(request):
    # pie_bike_status()
    return render(request, "bikeapp/pie_bike_status.html")


def dv_ustructure(request):
    # pie_User_Structure()
    return render(request, "bikeapp/pie_User_Structure.html")


def dv_monthpay(request):
    # bar_datazoom_Monthly_payment_quantity()
    return render(request, "bikeapp/bar_datazoom_Monthly_payment_quantity.html")


def dv_bikeusage(request):
    # liquid()
    return render(request, "bikeapp/liquid.html")


def dv_heatmappay(request):
    # heatmap_payment()
    return render(request, "bikeapp/heatmap_payment.html")


def dv_heatmapbike(request):
    # heatmap_bike()
    return render(request, "bikeapp/heatmap_bike.html")


def dv_rentbike(request):
    # bar_rent_duration()
    return render(request, "bikeapp/bar_rent_duration.html")

