from django.shortcuts import render,redirect
import mysql.connector as sql
from django.http import HttpResponseRedirect;


email=''

pwd=''
def emailsubmit(request):
    global email, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user='root', passwd="071418210016902", database='apana_motel')
        cursor=m.cursor();
        d=request.POST
        for key, value in d.items():
            if key =="email":
                email=value
            if key =="password":
                pwd=value
            
        c="select * from signin where Email='{}' and password='{}'".format(email,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
           return redirect('/order/')
            
    return render(request, 'email.html')








   