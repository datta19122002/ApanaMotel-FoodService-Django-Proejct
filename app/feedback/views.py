from django.shortcuts import render, redirect
import mysql.connector as sql
name=''
email=''
feedback=''
def feedbacks(request):
    global name, email, feedback
    if request.method=='POST':
        m=sql.connect(host='localhost', user='root', passwd='071418210016902', database='apana_motel')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='name':
                name=value;
            if key=='email':
                email=value
            if key=='feedback':
                feedback=value
        c = "insert into feedback values('{}','{}','{}')".format(name,email,feedback)
        cursor.execute(c)
        m.commit()
        return redirect('thankyoufb')
    return render(request, 'feedback.html')