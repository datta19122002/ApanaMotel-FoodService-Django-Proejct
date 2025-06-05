from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import mysql.connector as sql

name=''
ads=''
Pnum=''
email=''
fo=''
qty=0
fq=''

def ordernaw(request):
    global name, ads, Pnum, email, fo, fq, qty
    if request.method == 'POST':
        m=sql.connect(host='localhost', user='root', passwd='071418210016902', database='apana_motel')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == 'name':
                name = value
            if key == 'address':
                ads = value
            if key == 'phone':
                Pnum = value
            if key == 'email':
                email = value
            if key == 'food_order':
                fo=value
            if key=='food_rs':
                qty=value
            if key == 'food_quntity':
                fq = value;
        c = "insert into orderproduct values('{}','{}','{}','{}','{}','{}','{}')".format(name,ads,Pnum,email,fo,qty,fq)
        cursor.execute(c)
        m.commit()
        return redirect('thankyou')
    return render(request, 'order.html')


 


    
    

 