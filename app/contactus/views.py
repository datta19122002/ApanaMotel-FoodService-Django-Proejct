from django.shortcuts import render, redirect
import mysql.connector as sql
from django.http import HttpResponseRedirect
# Create your views here.
name=''
email=''
msg=''
def contactUs(request):
    global name, email, msg
    if request.method == 'POST':
        m=sql.connect(host='localhost', user='root', passwd='071418210016902', database='apana_motel')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == 'name':
                name=value
            if key == 'email':
                email=value
            if key == 'message':
                msg=value
        c="insert into contactform values('{}','{}','{}')".format(name,email,msg)
        cursor.execute(c)
        m.commit()
        return redirect('thankyoucu')
    return render(request, 'contact.html')