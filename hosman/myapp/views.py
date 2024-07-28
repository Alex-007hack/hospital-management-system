from django.shortcuts import render,redirect
from django .http import HttpResponse,HttpResponseRedirect
from ast import Return
from enum import Flag
from .models import Departments,Doctors,test,doc,leave,dratt,nus,nusleave,nuatt,accp,userreg,regcomp,userre,regcom
from .forms import BookingForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def accrej(request):
    return render(request,'accrej.html')
def main(request):
    return render(request,'main.html')
def confirm(request):
    return render(request,'confirm.html')
def leavecof(request):
    return render(request,'leavecof.html')
def attcof(request):
    return render(request,'attcof.html')
def nusmain(request):
    return render(request,'nusmain.html')
def mainlogin(request):
    return render(request,'mainlogin.html')
def createnu(request):
      if request.method == "POST":
        divname=request.POST['dname']
        divpass=request.POST['dpassword']
        divemail=request.POST['demail']
        nus.objects.create(nname=divname,npassword=divpass,nemail=divemail)
        return redirect("admin1")
      return render(request,'createnu.html')
def viewleave(request):
    details=leave.objects.all()
    return render(request,"viewleave.html",{'details':details})
def viewnusleave(request):
    de=nusleave.objects.all()
    return render(request,"viewnusleave.html",{'de':de})
def viewdrat(request):
    details1=dratt.objects.all()
    return render(request,"viewdrat.html",{'details1':details1})
def nusattview(request):
    d=dratt.objects.all()
    return render(request,"nusattview.html",{'d':d})
    
def sendatt(request):
    if request.method == "POST":
        datname=request.POST['dtname']
        datmail=request.POST['dtemail']
        datdate=request.POST['dtdate']
        datstatus=request.POST['dtstatus']
        datcomment=request.POST['dtcomment']
        dratt.objects.create(drname=datname,drmail=datmail,drdate=datdate,drstatus=datstatus,drcomment=datcomment)
       
        return redirect("attcof")
     
    return render(request,'sendatt.html')

    
def markatt(request):
    if request.method == "POST":
        datname=request.POST['dtname']
        datmail=request.POST['dtemail']
        datdate=request.POST['dtdate']
        datstatus=request.POST['dtstatus']
        datcomment=request.POST['dtcomment']
        nuatt.objects.create(drname=datname,drmail=datmail,drdate=datdate,drstatus=datstatus,drcomment=datcomment)
       
        return redirect("attcof")
     
    return render(request,'markatt.html')

def sendleave(request):
     if request.method == "POST":
        fmail=request.POST['frommail']
        fdate=request.POST['fromDate']
        tdate=request.POST['toDate']
        res=request.POST['reason']
        todaydate=request.POST['date']
        leave.objects.create(from_mail=fmail,from_date=fdate,to_date=tdate,idate=todaydate,reason=res)
       
        return redirect("leavecof")
     return render(request,'sendleave.html')
def sendnusleave(request):
     if request.method == "POST":
        fname=request.POST['fromName']
        fdate=request.POST['fromDate']
        tdate=request.POST['toDate']
        res=request.POST['reason']
        todaydate=request.POST['date']
        nusleave.objects.create(from_name=fname,from_date=fdate,to_date=tdate,idate=todaydate,reason=res)
       
        return redirect("leavecof")
     return render(request,'sendnusleave.html')
def d1(request):
    return render(request,'d1.html')
def about1(request):
    return render(request,'about1.html')
def drlogin(request):
    if request.method=='POST':
        mail=request.POST['drmail']
        passw=request.POST['drpassword']
        user=doc.objects.filter(demail=mail,dpassword=passw)
        if user:
            request.session['drmail']=mail 
            return redirect("docmain")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,'drlogin.html')
def nuslogin(request):
    if request.method=='POST':
        nmail=request.POST['drmail']
        npassw=request.POST['drpassword']
        nu=nus.objects.filter(nemail=nmail,npassword=npassw)
        if nu:
            request.session['drmail']=nmail 
            return redirect("nusmain")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,'nuslogin.html')
def docmain(request):
    return render(request,'docmain.html')
def call(request):
    return render(request,'call.html')
def login(request):
     adminuser="admin@gmail.com"
     pas="admin@123"
     if request.method=='POST':
        name=request.POST['mail']
        passw=request.POST['password']
        if name==adminuser and passw==pas:
            request.session=name
            return redirect("admin1")
        else:
            messages.error(request,"Invalid Credentials")
     return render(request,'login.html')
def about(request):
   return render(request,'about.html')
def testi(request):
   return render(request,'testimonial.html')
def dep(request):
   return render(request,'dep.html')
def admin1(request):
    return render(request,'admin1.html')
def createdr(request):
    if request.method == "POST":
        divname=request.POST['dname']
        divpass=request.POST['dpassword']
        divemail=request.POST['demail']
        doc.objects.create(dname=divname,dpassword=divpass,demail=divemail)
        return redirect("admin1")
    return render(request,'createdr.html')
   
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)
def contact(request):
     return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
def lab(request):
    dict_tests = {
        'tests': test.objects.all()
    }
    return render(request, 'lab.html', dict_tests)

def lea(request):
    # Get the doctor's profile using the logged-in user's ID
    doctor = get_object_or_404(Doctor, user=request.user)
    return render(request, 'doctor_profile.html', {'doctor': doctor})

def accrej(request):
    if request.method == "POST":
        astatus=request.POST['estatus']
        areason=request.POST['ereason']
        adate=request.POST['edate']
        accp.objects.create(acstatus=astatus,acreason=areason,acdate=adate)
        return redirect("admin1")
    return render(request,'accrej.html')

def myleave(request):
    deta=accp.objects.all()
    return render(request,"myleave.html",{'deta':deta})


def police_view_extraduty(request):
    l=doc.objects.filter(doc_id= request.session['police_id'])
    print(l)
    return render(request,"police_view_extraduty.html",{'l':l})

####
def userregister(request):
    if request.method=='POST':
        name=request.POST['name']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        mail=request.POST['email']
        phne=request.POST['mobile']
        usernameexists=userreg.objects.filter(username=name)
        emailexists=userreg.objects.filter(email=mail)
        if usernameexists:
            messages.error(request,"username already exsist")
        elif emailexists:
            messages.error(request,"Email already exsist")
        elif passw!=cpass:
            messages.error(request,"Password does not match")
        else:
            userreg.objects.create(username=name,password=passw,email=mail,phone=phne).save()
            return redirect("/")
    return render(request,"userregister.html")


def userlogin(request):
    if request.method=='POST':
        mail=request.POST['email']
        passw=request.POST['password']
        user=userreg.objects.filter(email=mail,password=passw)
        if user:
            request.session['email']=mail 
            return redirect("docmain")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,"userlogin.html")

def usercomp(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userreg.objects.get(email=current_user)
        
        if request.method=='POST':
            comparea=request.POST['rarea']
            compemail=request.POST['remail']
            compl=request.POST['rcomp']
            regcomp.objects.create(rarea=comparea,remail=compemail,rcomp=compl)
            return redirect("leavecof")
        return render(request,"usercomp.html",{'current_user':current_user,'user':user})
    return render(request,"usercomp.html")

def mycomplaint(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userreg.objects.get(email=current_user)
        complaintuser=regcomp.objects.filter(remail=user.email)
        return render(request,"mycomplaint.html",{'complaint':complaintuser})

def viewcomplaint(request):
    details=regcomp.objects.all()
    return render(request,"viewcomplaint.html",{'details':details})

def viewcomplaint2(request,id):
    complaint=regcomp.objects.get(id=id)
    if request.method=='POST':
        status=request.POST['Status']
        complaint.status=status
        complaint.save()
    return render(request,"complaint.html",{'regcomp':complaint})

def userregister1(request):
    if request.method=='POST':
        name=request.POST['name']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        mail=request.POST['email']
        phne=request.POST['mobile']
        usernameexists=userre.objects.filter(username=name)
        emailexists=userre.objects.filter(email=mail)
        if usernameexists:
            messages.error(request,"username already exsist")
        elif emailexists:
            messages.error(request,"Email already exsist")
        elif passw!=cpass:
            messages.error(request,"Password does not match")
        else:
            userre.objects.create(username=name,password=passw,email=mail,phone=phne).save()
            return redirect("admin1")
    return render(request,"userregister1.html")

def userlogin1(request):
    if request.method=='POST':
        mail=request.POST['email']
        passw=request.POST['password']
        user=userre.objects.filter(email=mail,password=passw)
        if user:
            request.session['email']=mail 
            return redirect("nusmain")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,"userlogin1.html")

def usercomp1(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userre.objects.get(email=current_user)
        
        if request.method=='POST':
            comparea=request.POST['rarea']
            compemail=request.POST['remail']
            compl=request.POST['rcomp']
            regcom.objects.create(rarea=comparea,remail=compemail,rcomp=compl)
            return redirect("leavecof")
        return render(request,"usercomp1.html",{'current_user':current_user,'user':user})
    return render(request,"usercomp1.html")

def mycomplaint1(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userre.objects.get(email=current_user)
        complaintuser=regcom.objects.filter(remail=user.email)
        return render(request,"mycomplaint1.html",{'complaint':complaintuser}) 

def viewcomplaint1(request):
    details=regcom.objects.all()
    return render(request,"viewcomplaint1.html",{'details':details})

def viewcomplaint3(request,id):
    complaint=regcom.objects.get(id=id)
    if request.method=='POST':
        status=request.POST['Status']
        complaint.status=status
        complaint.save()
    return render(request,"complaint1.html",{'regcom':complaint})




