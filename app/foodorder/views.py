from django.shortcuts import render
import mysql.connector as sql
from django.http import HttpResponseRedirect
# Create your views here.
fn=''
quntity=0
rs=0
address=''
name=''
email=''
phone=0
def orderfood(request):
    global fn, quntity, rs, address, name, email, phone
    if request.method=='POST':
        m=sql.connect(host='localhost', user='root', passwd='071418210016902', database='apana_motel')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=='fname':
                fn=value;
            if key=='food_quntity':
                quntity=value
            if key=='frs':
                rs=value
            if key=='caddress':
                address=value
            if key=='cname':
                name=value
            if key=='cemail':
                email=value
            if key=='cphone':
                phone=value
            c="insert into FoodOrder values('{}','{}','{}','{}','{}','{}','{}')".format(name, email, phone, fn, quntity, rs, address)
            cursor.execute(c)
            m.commit
    return render(request, 'order.html')

'''

uname=''

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
        
    return render(request, 'signinpage.html')
'''

