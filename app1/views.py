from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import registration,facprofile,stdprofile,subject,subjectallotment,feedbackreg,startfeedback,notes
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from random import randint
import smtplib
from django.core.mail import send_mail
from django.contrib import messages
import requests
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage




#FACULTY DASHBOARD
def uploadnotes(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        info=facprofile.objects.get(email=email)
        if request.method == 'POST' and request.FILES['document']:
            sname = request.POST['sname']
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            document = request.FILES['document']
            user=notes(sname=sname,programme=programme,branch=branch,sem=sem,document=document)
            user.save()
            messages.info(request, 'Notes Uploaded Successfully !!!!')
            return redirect('login')
        else:
            return render(request,'uploadnotes.html',{'user':info})
    else:
        return  redirect ('login')

def facsubwise(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        info=facprofile.objects.get(email=email)
        rating,count,one,two,three,four,five=0,0,0,0,0,0,0
        if request.method == "POST":
            sname = request.POST['sname']
            allrecord = feedbackreg.objects.filter(sname=sname)
            for records in allrecord:
                r=records.overall
                rating=rating + float(r)
                o=records.ques1
                one=one + float(o)
                tw=records.ques2
                two=two + float(tw)
                th=records.ques3
                three=three + float(th)
                fo=records.ques4
                four=four + float(fo)
                fi=records.ques5
                five=five + float(fi)
                count=count + 1
            rating=rating/count
            rating= round(rating,2)
            one=one/count
            one= round(one,2)
            two=two/count
            two= round(two,2)
            three=rating/count
            three= round(three,2)
            four=four/count
            four= round(four,2)
            five=five/count
            five= round(five,2)
            context = {'allrecord': allrecord,'user':info,'rating':rating,'sname':sname,'one':one,'two':two,'three':three,'four':four,'five':five}
            return render(request, 'showfacsubwise.html', context)
    else:
        return redirect('login')



def faclogin(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        if facprofile.objects.filter(email=email).exists():
            facinfo = facprofile.objects.get(email=email)
            facname=facinfo.name
            facsub = subjectallotment.objects.filter(tname=facname)
            return render(request, 'facdash.html',{'stdinfo':facinfo,'user':facinfo,'facsubs':facsub})
        else:
            messages.info(request, 'Profile Not Updated Please Update Your Profile !!!!')
            return redirect('login')
    else:
        return redirect('login')

def facupdateprofile(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        if facprofile.objects.filter(email=email).exists():
            info= facprofile.objects.get(email=email)
            context={'user':info}
        else:
            info= registration.objects.get(email=email)
            context={'user':info}
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            add = request.POST['add']
            spec = request.POST['spec']
            email = request.POST['email']
            branch = request.POST['branch']
            if facprofile.objects.filter(email=email).update(phone=phone,branch=branch,add=add,spec=spec):
                messages.info(request, 'Profile Updated Successfully !!!!')
                return redirect('login')
            else:
                user=facprofile(name=name,phone=phone,add=add,spec=spec,branch=branch,email=email)
                user.save()
                messages.info(request, 'Profile Updated Successfully !!!!')
                return redirect('login')
        else:
            return render(request,'facupdateprofile.html',context)
    else:
        return  redirect ('login')

def facviewprofile(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        if facprofile.objects.filter(email=email).exists():
            info= facprofile.objects.get(email=email)
            context={'user':info}
            return render(request,'facviewprofile.html',context)
        else:
            info= registration.objects.get(email=email)
            context={'user':info}
            return render(request,'facviewprofile.html',context)
    else:
        return  redirect ('login')





















#STUDENT DASHBOARD
def downloadnotes(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if stdprofile.objects.filter(email=email).exists():
            user= stdprofile.objects.get(email=email)
            programme=user.programme
            branch=user.branch
            sem=user.sem
            allrecords=notes.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem).all()
            return render(request, 'downloadnotes.html', {'allrecords': allrecords,'user':user})
        else:
            messages.info(request, 'Profile Not Updated Please Update Your Profile !!!!')
            return redirect('login')
    else:
        return  redirect ('login')

def stdupdateprofile(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        info= registration.objects.get(email=email)
        context={'user':info}
        if request.method == 'POST':
            name = request.POST['name']
            fname = request.POST['fname']
            roll = request.POST['roll']
            phone = request.POST['phone']
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            email = request.POST['email']
            if stdprofile.objects.filter(email=email).update(name=name,fname=fname,phone=phone):
                messages.info(request, 'Profile Updated Successfully !!!!')
                return redirect('login')
            else:
                user=stdprofile(name=name,fname=fname,roll=roll,phone=phone,programme=programme,branch=branch,sem=sem,email=email)
                user.save()
                messages.info(request, 'Profile Updated Successfully !!!!')
                return redirect('login')
        else:
            return render(request,'stdupdateprofile.html',context)
    else:
        return  redirect ('login')

def stdviewprofile(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if stdprofile.objects.filter(email=email).exists():
            info= stdprofile.objects.get(email=email)
            context={'user':info}
            return render(request,'stdviewprofile.html',context)
        else:
            info= registration.objects.get(email=email)
            context={'user':info}
            return render(request,'stdviewprofile.html',context)
    else:
        return  redirect ('login')

def preevfeed(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if stdprofile.objects.filter(email=email):
            user= stdprofile.objects.get(email=email)
            id=user.id
            allrecord = feedbackreg.objects.filter(stdid=id).all
            context={'allrecord':allrecord,'user':user}
            return render(request,'prevfdbk.html',context)
        else:
            messages.info(request, 'Please Update Your Profile !!!!')
            return redirect('login')
    else:
        return  redirect ('login')

def checkotp(request):
    if request.session.has_key('std_logged'):
        if request.method == 'POST':
            id = request.POST['id']
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            pwd = request.POST['pwd']
            data = stdprofile.objects.get(id=id)
            context1 = {'id': data.id, 'name': data.name, 'fname': data.fname, 'roll': data.roll, 'phone': data.phone,
                        'programme': data.programme, 'branch': data.branch, 'sem': data.sem, 'email': data.email,}
            if startfeedback.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem).filter(pwd=pwd).exists():
                if subjectallotment.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem).exists:
                    data1 = subjectallotment.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem)
                    context ={'id': data.id,'programme':programme,'branch':branch,'sem':sem,'data1': data1}
                    return render(request, 'givefeedback.html',context)
                    #return HttpResponse(data[2])
            else:
                messages.info(request, 'Sorry Wrong OTP Password !!!!')
                return redirect('login')
        else:
            return redirect('validateotp')
    else:
        return  redirect ('login')

def validateotp(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if stdprofile.objects.filter(email=email).exists():
            data = stdprofile.objects.get(email=email)
            info = stdprofile.objects.get(email=email)
            return render(request,'validateotp.html',{'user': info,'id':data.id,'name': data.name,'fname': data.fname,'roll': data.roll,'phone': data.phone,'programme': data.programme,'branch': data.branch,'sem': data.sem,'email': data.email})
        else:
            messages.info(request, 'Profile Not Updated Please Update Your Profile !!!!')
            return redirect('login')
    else:
        return  redirect ('login')

def feedreg(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        info = registration.objects.get(email=email)
        if request.method == 'POST':
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            stdid = request.POST['stdid']
            sname = request.POST['sname']
            data=subjectallotment.objects.filter(sname=sname)
            for record in data:
                tname=record.tname
            ques1 = request.POST['ques1']
            ques2 = request.POST['ques2']
            ques3 = request.POST['ques3']
            ques4 = request.POST['ques4']
            ques5 = request.POST['ques5']
            tot = int(ques1)+int(ques2)+int(ques3)+int(ques4)+int(ques5)
            overall=tot/5
            if feedbackreg.objects.filter(programme=programme).filter(branch=branch).filter(sname=sname).filter(sem=sem).filter(stdid=stdid).exists():
                messages.info(request, 'Already Submitted The Feedback !!!!')
                return redirect('login')
            else:
                user = feedbackreg(programme=programme, branch=branch, sem=sem, stdid=stdid, sname=sname,tname=tname,ques1=ques1, ques2=ques2, ques3=ques3, ques4=ques4, ques5=ques5,overall=overall)
                user.save()
                messages.info(request, 'Submitted Successfully !!!!')
                return redirect('login')
    else:
        return  redirect ('login')








#ADMIN DASHBOARD
def allotsub(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        if request.method == "POST":
            branch = request.POST['branch']           
            allsubject = subject.objects.values('name').distinct().filter(branch=branch)
            allfaculty = facprofile.objects.values('name').distinct().filter(branch=branch)
            context = {'allsubject': allsubject,'allfaculty':allfaculty,'user':info}
            return render(request, 'allotsub.html',context)
        else:
            return render(request, 'adminselectbranch.html',{'user':info})
    else:
        return  redirect ('login')

def subalmt(request):
    if request.method == "POST":
        sname = request.POST['sname']
        tname = request.POST['tname']
        programme = request.POST['programme']
        branch = request.POST['branch']
        sem = request.POST['sem']
        user = subjectallotment(sname=sname,tname=tname,programme=programme,branch=branch,sem=sem)
        user.save()
        messages.info(request, 'Alloteded Successfully !!!!')
        return redirect('login')

def start_feedback(request):
    if request.method == 'POST':
        programme = request.POST['programme']
        branch = request.POST['branch']
        sem = request.POST['sem']
        pwd = request.POST['pwd']
        if startfeedback.objects.filter(programme=programme,branch=branch,sem=sem).update(pwd=pwd):
            messages.info(request, 'Your Password OTP Is Ready To Take Feedback !!!!')
            return redirect('login')
        else:
            user = startfeedback(programme=programme, branch=branch, sem=sem, pwd=pwd)
            user.save()
            messages.info(request, 'Your Password OTP Is Ready To Take Feedback !!!!')
            return redirect('login')

def subreg(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        branch = request.POST['branch']
        if subject.objects.filter(code=code).exists():
            messages.info(request, 'Subject Already Registered !!!!')
            return redirect('login')
        else:
            user = subject(name=name,code=code,branch=branch)
            user.save()
            messages.info(request, 'Subject Added Successfully !!!!')
            return redirect('login')

def strtfeed(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        return render(request, 'strtfeed.html',{'user':info})
    else:
        return  redirect ('login')

def addsub(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        return render(request, 'addsub.html',{'user':info})
    else:
        return  redirect ('login')

def addfac(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        return render(request, 'addfac.html',{'user':info})
    else:
        return  redirect ('login')

def viewfac(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        if request.method == "POST":
            branch = request.POST['branch']
            allrecord = facprofile.objects.all().filter(branch=branch)
            return render(request, 'viewfac.html',{'user':info,'allrecord': allrecord})
        else:
            return render(request, 'adminselectbranchfeed.html',{'user':info})
    else:
        return  redirect ('login')

def viewstd(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        if request.method == "POST":
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            allrecord = stdprofile.objects.all().filter(programme=programme,branch=branch,sem=sem)
            return render(request, 'viewstd.html',{'user':info,'allrecord': allrecord})
        else:
            return render(request, 'adminselectstdfeed.html',{'user':info})
    else:
        return  redirect ('login')

def viewsub(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        allrecord = subject.objects.all()
        info = registration.objects.get(email=email)
        return render(request, 'viewsub.html',{'user':info,'allrecord': allrecord})
    else:
        return  redirect ('login')

def viewalmt(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        allrecord = subjectallotment.objects.all()
        info = registration.objects.get(email=email)
        return render(request, 'viewalmt.html',{'user':info,'allrecord': allrecord})
    else:
        return  redirect ('login')

def viewfeedback(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        if request.method == 'POST':
            programme = request.POST['programme']
            branch = request.POST['branch']
            sem = request.POST['sem']
            data = feedbackreg.objects.filter(programme=programme,branch=branch,sem=sem)
            context={'programme':programme,'branch':branch,'sem':sem,'data':data,'user':info}
            return render(request,'feedback1.html',context)
    else:
        return  redirect ('login')

def subfeed(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        if request.method == 'POST':
            sname = request.POST['sname']
            allrecord=feedbackreg.objects.filter(sname=sname)
            context = {'allrecord': allrecord,'user':info}
            return render(request, 'subfeed.html', context)
    else:
        return  redirect ('login')

def subwisefeed(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        allsubject = subject.objects.values('name').distinct()
        context = {'allsubject': allsubject,'user':info}
        if request.method == "POST":
            sname = request.POST['sname']
            allrecord = feedbackreg.objects.filter(sname=sname)
            contexts = {'allrecord': allrecord}
            return render(request, 'showsubwise.html', contexts)
        else:
            return render(request,'subwisefeed.html',context)
    else:
        return  redirect ('login')

def facwisefeed(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        allfac = facprofile.objects.values('name').distinct()
        context = {'allfac': allfac,'user':info}
        if request.method == "POST":
            tname = request.POST['tname']
            allrecord = feedbackreg.objects.filter(tname=tname)
            contexts = {'allrecord': allrecord}
            return render(request, 'showfacwise.html', contexts)
        else:
            return render(request,'facwisefeed.html',context)
    else:
        return  redirect ('login')

def viewfeed(request):
    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        return render(request, 'viewfeed.html',{'user':info})
    else:
        return  redirect ('login')

def index(request):
    return  render (request,'index.html')

def about(request):
    return  render (request,'about.html')

def course(request):
    return  render (request,'course.html')

def element(request):
    return  render (request,'element.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        email1='vikrantgroupofinstitutionsgwal@gmail.com'
        name = request.POST['name']
        msg = request.POST['msg']
        mobile = request.POST['mobile']
        body='Name = ' + str(name) + '\n' +'Mobile Number = ' + str(mobile) + '\n' + 'Email = ' + str(email) +  '\n' + 'Message = ' + str(msg) + '..' 
        subject='VIKRANT GROUP OF INSTITUTIONS'
        bod='Thank You For Contacting Vikrant Group Of Institutions We Will Get in Touch With You Shortly--'
        send_mail(subject,bod,'vikrantgroupofinstitutionsgwal@gmail.com',[email],fail_silently=False)
        send_mail(subject,body,'vikrantgroupofinstitutionsgwal@gmail.com',[email1],fail_silently=False)
        return redirect('index')
    else:
        return  render (request,'contact.html')

    

def fshowsub(request):
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        if facprofile.objects.filter(email=email).exists():
            info = facprofile.objects.get(email=email)
            return render(request, 'fshowsub.html',{'user':info})
    else:
        return  redirect ('login')

def stdlogout(request):
    del request.session['std_logged']
    return redirect('index')
def alogout(request):
    del request.session['a_logged']
    return redirect('index')
def faclogout(request):
    del request.session['fac_logged']
    return redirect('index')


def register(request):
    if request.method == 'POST':
        code = request.POST['code']
        code1="0936"
        code4="0936a"
        code5="0936A"
        code3="0936F"
        email = request.POST['email']
        pwd = request.POST['pwd']
        rpwd = request.POST['rpwd']
        code2="0936f"
        subject='VIKRANT GROUP OF INSTITUTIONS'
        bod='Your Four Digits One Time Password OTP For Registration In VIKRANT FEEDBACK SYSTEM Is--'
        otp= generate(4)
        message = f'{otp}'
        body= bod + str(otp)
        context={'code':code,'email':email,'pwd':pwd,'totp':otp}
        if code==code1 or code==code2 or code==code3 or code==code4 or code==code5:
            if pwd==rpwd:
                if registration.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist !!!!')
                    return redirect('register')
                else:
                    send_mail(subject,body,'vikrantgroupofinstitutionsgwal@gmail.com',[email],fail_silently=False)
                    return render(request,'password.html',context)
            else:
                messages.info(request, 'Both Passwords Are Not Same !!!!')
                return redirect('register')
        else:
            messages.info(request, 'Enter Valid User Code !!!!')
            return redirect('register')
    else:
        return render(request,'register.html')

def generate(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#ONE TIME PASSWORD
def validate(request):
    if request.method == 'POST':
        code = request.POST['code']
        email = request.POST['email']
        pwd = request.POST['pwd']
        otp = request.POST['otp']
        totp = request.POST['totp']
        if otp==totp:
            if registration.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist !!!!')
                    return redirect('register')
            user = registration(code=code,email=email, pwd=pwd)
            user.save()
            messages.info(request, 'Registered Successfully Login To Continue !!!!')
            return redirect('login')
        else:
            messages.info(request, 'OTP Is Not Correct !!!!')
            return redirect('validate')
    else:
        return render(request,'password.html')

def generate(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#ONE TIME PASSWORD
def validate(request):
    if request.method == 'POST':
        code = request.POST['code']
        email = request.POST['email']
        pwd = request.POST['pwd']
        otp = request.POST['otp']
        totp = request.POST['totp']
        if otp==totp:
            if registration.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist !!!!')
                    return redirect('register')
            user = registration(code=code,email=email, pwd=pwd)
            user.save()
            messages.info(request, 'Registered Successfully Login To Continue !!!!')
            return redirect('login')
        else:
            messages.info(request, 'OTP Is Not Correct !!!!')
            return redirect('validate')
    else:
        return render(request,'password.html')

# LOGIN
def login(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if stdprofile.objects.filter(email=email).exists():
            info = stdprofile.objects.get(email=email)
            return render(request, 'stdlogin.html',{'user':info})
        else:
            info = registration.objects.get(email=email)
            return render(request, 'stdlogin.html',{'user':info})
        
    
    if request.session.has_key('fac_logged'):
        email = request.session.get('fac_logged')
        if facprofile.objects.filter(email=email).exists():
            info = facprofile.objects.get(email=email)
            facinfo = facprofile.objects.get(email=email)
            facname=facinfo.name
            facsub = subjectallotment.objects.filter(tname=facname)
            return render(request, 'faclogin.html',{'user':info,'facsub':facsub})
        else:
            info = registration.objects.get(email=email)
            return render(request, 'faclogin.html',{'user':info})

    if request.session.has_key('a_logged'):
        email = request.session.get('a_logged')
        info = registration.objects.get(email=email)
        scount = stdprofile.objects.all().count()
        tcount = facprofile.objects.all().count()
        subcount = subject.objects.all().count()
        feedcount = feedbackreg.objects.all().count()
        return render(request, 'alogin.html',{'user':info,'scount':scount,'tcount':tcount,'subcount':subcount,'feedcount':feedcount})

    if request.method == 'POST':
        email = request.POST['email']
        code1="0936"
        code2="0936f"
        code3="0936F"
        code4="0936a"
        code5="0936A"
        pwd = request.POST['pwd']
        if registration.objects.filter(email=email).filter(pwd=pwd).exists():
            info1 = registration.objects.get(email=email)
            code=info1.code
            if code==code1:
                request.session['std_logged'] = email
                if stdprofile.objects.filter(email=email).exists():
                    info = stdprofile.objects.get(email=email)
                    return render(request, 'stdlogin.html',{'user':info})
                else:
                    info = registration.objects.get(email=email)
                    return render(request, 'stdlogin.html',{'user':info})
            if code==code2:
                request.session['fac_logged'] = email
                if facprofile.objects.filter(email=email).exists():
                    info = facprofile.objects.get(email=email)
                    facinfo = facprofile.objects.get(email=email)
                    facname=facinfo.name
                    facsub = subjectallotment.objects.filter(tname=facname)
                    return render(request, 'faclogin.html',{'user':info,'facsub':facsub})
                else:
                    info = registration.objects.get(email=email)
                    return render(request, 'faclogin.html',{'user':info})
            if code==code3:
                request.session['fac_logged'] = email
                if facprofile.objects.filter(email=email).exists():
                    info = facprofile.objects.get(email=email)
                    facinfo = facprofile.objects.get(email=email)
                    facname=facinfo.name
                    facsub = subjectallotment.objects.filter(tname=facname)
                    return render(request, 'faclogin.html',{'user':info,'facsub':facsub})
                else:
                    info = registration.objects.get(email=email)
                    return render(request, 'faclogin.html',{'user':info})
            if code==code4:
                request.session['a_logged'] = email
                info = registration.objects.get(email=email)
                scount = stdprofile.objects.all().count()
                tcount = facprofile.objects.all().count()
                subcount = subject.objects.all().count()
                feedcount = feedbackreg.objects.all().count()
                return render(request, 'alogin.html',{'user':info,'scount':scount,'tcount':tcount,'subcount':subcount,'feedcount':feedcount})
            if code==code5:
                request.session['a_logged'] = email
                info = registration.objects.get(email=email)
                scount = stdprofile.objects.all().count()
                tcount = facprofile.objects.all().count()
                subcount = subject.objects.all().count()
                feedcount = feedbackreg.objects.all().count()
                return render(request, 'alogin.html',{'user':info,'scount':scount,'tcount':tcount,'subcount':subcount,'feedcount':feedcount})
            
        else:
            messages.info(request, 'Please Enter Valid Credentials !!!!')
            return redirect('login')
    else:
        return render(request,'login.html')



def recovery(request):
    if request.method == 'POST':
        email = request.POST['email']
        if registration.objects.filter(email=email).exists():
            info = registration.objects.get(email=email)
            subject='VIKRANT GROUP OF INSTITUTIONS'
            bod='Your Password For Login In VIKRANT FEEDBACK SYSTEM Is--'
            body= bod + str(info.pwd)
            send_mail(subject,body,'vikrantgroupofinstitutionsgwal@gmail.com',[email],fail_silently=False)
            messages.info(request, 'Password Is Sent To Your Registered E-Mail Id !!!!')
            return redirect('login')
        else:
            messages.info(request, 'Email Not Registered Register It From Here !!!!')
            return redirect('register')
    else:
        return render(request,'recovery.html')



#DELETE
def stddelete(request,id):
    print(id)
    stdprofile.objects.filter(id=id).delete()
    return redirect("login")



def almtdelete(request,id):
    print(id)
    subjectallotment.objects.filter(id=id).delete()
    return redirect("login")



def facdelete(request,id):
    print(id)
    facprofile.objects.filter(id=id).delete()
    return redirect("login")



def subdelete(request,id):
    print(id)
    subject.objects.filter(id=id).delete()
    return redirect("login")

