import mysql.connector as sql 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect 
uname=''
dob=''
gender=''
email=''
phone=''
pwd=''

def signpage(request):
    global uname, dob, gender, email, phone, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user='root', passwd="071418210016902", database='apana_motel')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="username":
                uname=value
            if key =="gender":
                gender=value
            if key =="email":
                email=value;
            if key =="phone":
                phone=value
            if key =="password":
                pwd=value
            
        c="INSERT INTO signin VALUES('{}','{}','{}','{}','{}')".format(uname, gender, email, phone, pwd)
        cursor.execute(c)
        m.commit()
        t=tuple(cursor.fetchall())
        return redirect('/index/')      
    return render(request, 'signinpage.html')