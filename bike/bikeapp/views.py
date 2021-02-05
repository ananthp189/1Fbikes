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

def login(request):
    return render(request,'bikeapp/login.html')

# 注册界面


def register(request):
    return render(request,'bikeapp/register.html')

def main(request):
    return render(request,'bikeapp/main_page_map.html')


# 注册函数 save方法

def save(request):
    has_register = 0#用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.GET#获取get()请求
    #print(a)
    #通过get()请求获取前段提交的数据
    userID = a.get('UserID')
    name = a.get('Name')
    password = a.get('Password')
    telephone = a.get('Telephone')
    bankcard = a.get('Bankcard')

    #print(userName,passWord)
    #连接数据库
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    #创建游标
    cursor = db.cursor()
    #SQL语句
    sql1 = 'select * from Users'
    #执行SQL语句
    cursor.execute(sql1)
    #查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userID in all_users[i]:
            ##表示该账号已经存在
            has_register = 1

        i += 1
    if has_register == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into Users(uid,uname,upassword,Tel,bankcard) values(%s,%s,%s,%s,%s)'
        cursor.execute(sql2, (userID, name, password, telephone, bankcard))
        db.commit()
        # 需要修改数据库中的语句时，增，删，改... ，加上commit
        cursor.close()
        db.close()
        # tkinter.messagebox.showerror("提示","恭喜您，注册用户成功！")
        # return HttpResponse('注册成功')
        return render(request, 'bikeapp/register_succeed.html', {'has_register':has_register, 'userName': name})

    # else:
    if has_register == 1:
        cursor.close()
        db.close()
        # tkinter.messagebox.showerror("提示","抱歉，用户名重复，注册失败")
        # return HttpResponse('该账号已存在')
        return render(request, 'bikeapp/register_succeed.html', {'has_register': has_register, 'userName': name})
# 登陆函数 query方法


def query(request):
    a = request.GET
    userid = a.get('userID')
    password = a.get('password')
    user_tup = (userid, password)
    global ID
    ID = userid
    # 定义全局变量！！！！！！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
    cursor = db.cursor()
    # 获取操作游标
    sql = 'select uid,upassword from Users'
    cursor.execute(sql)
    # 执行sql语句
    all_users = cursor.fetchall()
    # 查询结果全部返回
    cursor.close()
    # 关闭游标
    db.close()
    # 关闭数据库
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
        # 查询用户账户的姓名
        # (host="localhost", user="root", password="xxx", database="xxxx")
        db = pymysql.connect(host='localhost', user='root', password='123123', database='bikerental')
        cursor2 = db.cursor(pymysql.cursors.DictCursor)
        sql1 = 'select uname from Users where uid ="{}"'
        sql2 = sql1.format(userid)
        cursor2.execute(sql2)
        username = cursor2.fetchall()
        cursor2.close()
        db.close()
        global username1
        username1 = username
        # 定义全局变量！！！！！!!!!!!!!!!
        return render(request, 'bikeapp/main_page_map.html', {'has_user': has_user, 'userName': username})

     # return HttpResponse('登录成功')
    else:
        return render(request, 'bikeapp/login.html', {'has_user': has_user})
        # return HttpResponse('用户名或密码有误')
