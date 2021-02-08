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


# login webpage
def login(request):
    return render(request,'bikeapp/login.html')

# register page
def register(request):
    return render(request,'bikeapp/register.html')

def main(request):
    return render(request,'bikeapp/main_page_map.html')


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
    db = pymysql.connect('localhost', 'root', '19990124', 'bikerental')
    #create cursor
    cursor = db.cursor()
    #SQL sentence
    sql1 = 'select * from Users'
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
        sql2 = 'insert into Users(uid,uname,upassword,Tel,bankcard) values(%s,%s,%s,%s,%s)'
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
    db = pymysql.connect('localhost', 'root', '19990124', 'bikerental')
    cursor = db.cursor()
    # Get operation cursor
    sql = 'select uid,upassword from Users'
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
        db = pymysql.connect('localhost', 'root', '19990124', 'bikerental')
        cursor2 = db.cursor(pymysql.cursors.DictCursor)
        sql1 = 'select uname from Users where uid ="{}"'
        sql2 = sql1.format(userid)
        cursor2.execute(sql2)
        username = cursor2.fetchall()
        cursor2.close()
        db.close()
        global username1
        username1 = username
        # Define global variables! ! ! ! ! ! !!!!!!!!
        return render(request, 'bikeapp/main_page_map.html', {'has_user': has_user, 'userName': username})

     # return HttpResponse('login success')
    else:
        return render(request, 'bikeapp/login.html', {'has_user': has_user})
        # return HttpResponse('password or username wrong!')