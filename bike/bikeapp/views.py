import json
import math
import time

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import pymysql.cursors
import os
from django.http import StreamingHttpResponse
from django.conf import settings
import urllib.parse
import random


# login webpage
def login(request):
    return render(request,'bikeapp/login.html')

# register page
def register(request):
    return render(request,'bikeapp/register.html')

def main(request):
    return render(request,'bikeapp/index.html')


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
        sql2 = 'insert into customer_info(ID,UserName,Password,Tel,Bankcard) values(%s,%s,%s,%s,%s)'
        cursor.execute(sql2, (userID, name, password, telephone, bankcard))
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
        print("!!!!!!!!!!!!!!!!!!!!!!")
        print(all_users[i])
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
        print("############################")
        print(has_user)
    if has_user == 1:
        # Query the name of the user account
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor2 = db.cursor(pymysql.cursors.DictCursor)
        sql1 = 'select UserName from customer_info where ID ="{}"'
        sql2 = sql1.format(userid)
        cursor2.execute(sql2)
        username = cursor2.fetchall()
        cursor2.close()
        db.close()
        global username1
        username1 = username
        # Define global variables! ! ! ! ! ! !!!!!!!!
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
        status = 2  # set bike status = 2 (1 good, 2 broken)
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
    bID = 102 # get from rentbike function set a global various
    payid = random.sample(range(10002,11000),1)
    # set payment status
    status = 0
    # duration
    totaltime = 612
    start = 1201
    end = 1306
    bduration = end - start
    count = bduration // 100           # get the hour
    original_bill = count * 0.5         # 0.5 pounds an hour
    if totaltime >= 500:
        discount_bill = original_bill * 0.8   # discount, 80% off
    else:
        discount_bill = original_bill      # no discount
        # Update Database

    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # Create cursor
    cursor = db.cursor()
    sql2 = 'insert into pay_info(pID,pstatus,starttime, endtime, duration, oribill, discount, ID, bID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql2, (payid, status, start, end, bduration, original_bill, discount_bill,ID, bID))
    db.commit()
    cursor.close()
    db.close()

    #Return value
    p = request.GET
    submit1 = p.get('subtype')
    if submit1 == 1:
        put = 1
        status = 1
        buse = 0  # in bike chart
        totaltime = totaltime + count * 60 + (bduration % 100)

    # Update the databse

    #Update payment
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    sql3 = 'UPDATE pay_info SET pstatus=%s where pID=%s'
    cursor.execute(sql3, (status, payid))
    db.commit()

    #Update user time
    sql3 = 'UPDATE customer_info SET renttime=%s where ID=%s'
    cursor.execute(sql3, (totaltime, ID))
    db.commit()

    # Update bike status
    sql4 = 'UPDATE bike_info SET bstatus=%s where bID=%s'
    cursor.execute(sql4, (buse, bID))
    db.commit()
    cursor.close()
    db.close()

    return render(request,'bikeapp/pay.html', {'payid': payid, 'time': count, 'original_bill': original_bill, 'discount_bill': discount_bill, 'put':put })


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



###########movebike-collect data########

def movebike(request):
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    # add “pymysql.cursors.DictCursor” to pass variables to web-front
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = 'select bID, bstatus, bGPSx,bGPSy, barea, busage from bike_info'
    cursor.execute(sql)
    # All data from the database
    all_bikes = cursor.fetchall()

    ###################li------add-----------
    area_list = []
    for a in all_bikes:
        area_list.append(a['barea'])
    result = dict()
    for b in set(area_list):
        result[b] = area_list.count(b)
    print(list(result.items()))
    #Assuming that there are 80 bikes in each area, the area with insufficient vehicles is displayed
    normal = 80
    warn_list = []
    for i in result.items():
        if i[1] < normal:
            y = "area " + i[0] + " needs more bikes!!!!"
            print(y)
            warn_list.append(y)
        else:
            x = "area " + i[0] + " is good"
            print(x)
            warn_list.append(x)
    #print(warn_list)
    ######################
    #close cursor
    cursor.close()
    #close database
    db.close()

    # print(all_bikes)
    return render(request, 'bikeapp/movebike.html',{'allbikes': all_bikes, 'result': result.items(),'warn':warn_list})


#---------------movebike_action--------#
# def move(request):
#     a = request.GET
#     move_bid = a.get('bid')
#     move_area = a.get('barea')
#     global gpsx, gpsy
#     if move_area == 'A':
#         gpsx = random.uniform(55.85,55.90)
#         gpsy = random.uniform(-4.15,-4.26)
#     elif move_area == 'B':
#         print("aaaaaaaaaa")
#         gpsx = random.uniform(55.90,55.95)
#         gpsy = random.uniform(-4.26,-4.31)
#     elif move_area == 'C':
#         gpsx = random.uniform(55.90,55.95)
#         gpsy = random.uniform(-4.0,-4.15)
#     elif move_area == 'D':
#         gpsx = random.uniform(55.81,55.85)
#         gpsy = random.uniform(-4.26,-4.31)
#     elif move_area == 'E':
#         gpsx = random.uniform(55.81,55.85)
#         gpsy = random.uniform(-4.0,-4.15)
#     gpsx = str(gpsx)
#     gpsy = str(gpsy)
#     print("GPS！！", gpsx)
#     db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
#     cursor = db.cursor()
#     sql = 'update bike_info set barea=%s where bID=%s'
#     cursor.execute(sql, (move_area, move_bid))
#     db.commit()
#     cursor.close()
#     db.close()
#
#     db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
#     cursor = db.cursor()
#     sql2 = 'update bike_info set bGPSx=%s,bGPSy=%s where bID=%s'
#     cursor.execute(sql2, (gpsx, gpsy, move_bid))
#     db.commit()
#     cursor.close()
#     db.close()
#     return HttpResponse('succeed')


#----------------select-------------------

def select(request):
    a = request.POST
    #b = request.REQUEST.get
    select_move_bid = request.POST.getlist('select_bid')
    print("Here！！！", select_move_bid)
    select_move_area = a.get('select_barea')
    print(select_move_area)
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    for i in select_move_bid:
         #Randomly generated gps
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
    #text
    # print(select_move_bid)
    return render(request, 'bikeapp/movebike.html',{'move_area': json.dumps(select_move_area)})





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
    cursor.execute("SELECT * FROM customer_info WHERE ID = %s", int(ID))
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

    cursor.execute("UPDATE bike_info SET busage = 1 WHERE bID = %s", int(bike["bID"]))
    db.commit()


    # with global id get user
    # assign bike based on user area
    # record start time
    sql2 = "INSERT INTO pay_info (ID, bID, starttime, startGPSx, startGPSy) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql2, (user["ID"], bike["bID"], time.time(), bike["bGPSx"], bike["bGPSy"]))

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

    # Get user and bike details from global id
    cursor.execute("SELECT * FROM customer_info WHERE ID = %s", int(ID))
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM bike_info WHERE ID = %s", int(BID))
    bike = cursor.fetchone()

    # set the fetched bike to returned status

    cursor.execute("UPDATE bike_info SET busage = 0 WHERE bID = %s", int(BID))
    db.commit()
    # return bike based on user current location
    # record end time and update the table
    sql2 = "update pay_info ( endtime, endGPSx, endGPSy) VALUES ( %s, %s, %s) where  id= %s and bID= %s"
    cursor.execute(sql2, time.time(), user["uGPSx"], user["uGPSy"], int(ID), int(BID))

    # assign charge and discount
    pay()

    bikeid = bike["bID"]
    return render(request, 'bikeapp/returnbike.html',{'bike_id': bikeid})  ,






