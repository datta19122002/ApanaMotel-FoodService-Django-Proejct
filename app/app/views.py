from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import mysql.connector as sql
from .forms import signupform

def index(request):
    return render(request, 'index.html')
name=''
email=''
msg=''

def contact(request):
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


def about(request):
    return render(request, 'about.html')

def thankyou(request):
    return render(request, 'thankyou.html')
def addition(request):
    ans=0
    try:
        n1=int(request.GET.get('num1'))
        n2=int(request.GET.get('num2'))
        ans=n1+n2
    except:
        pass
    return render(request, 'addition.html',{'output':ans})


def Try(request):
    return render(request,'try.html')
def thankyoufb(request):
    return render(request, 'thankyoufb.html')


def thankyoucu(request):
    return render(request, 'thankyoucs.html')



def search(request):
    return HttpResponse('This is the search bar')












