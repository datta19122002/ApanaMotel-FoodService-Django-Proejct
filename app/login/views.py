from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import response
import mysql.connector as sql

uname=''
pwd=''

def loginpage(request):
    global uname, pwd
    if request.method=="POST":
        m=sql.connect(host='localhost', user='root', passwd='071418210016902', database='apana_motel')
        cursor=m.cursor();
        d=request.POST
        for key, value in d.items():
            if key == "username":
                uname=value
            if key == "password":
                pwd = value
                
        c="select * from signin where User_Name='{}' and password='{}'".format(uname, pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
            return redirect('/index/')
            
    return render(request, 'loginpage.html')





