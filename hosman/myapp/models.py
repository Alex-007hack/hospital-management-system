from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' +  self.doc_name + ' - (' + self.doc_spec + ')'



class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class test(models.Model):
    test_name = models.CharField(max_length=100)
    test_decription = models.TextField()

class doc(models.Model):
    dname=models.CharField(max_length=25)
    dpassword=models.CharField(max_length=25)
    demail=models.CharField(max_length=25)

class leave(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('declained','Declained'),
    ]

    from_mail=models.CharField(max_length=200,default="")
    from_date=models.CharField(max_length=200)
    to_date=models.CharField(max_length=200)
    idate=models.CharField(max_length=200) 
    reason=models.CharField(max_length=200) 
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

class dratt(models.Model):
    drname=models.CharField(max_length=200)
    drmail=models.CharField(max_length=200)
    drdate=models.CharField(max_length=200)
    drstatus=models.CharField(max_length=200)
    drcomment=models.CharField(max_length=200)

class nus(models.Model):
    nname=models.CharField(max_length=25)
    npassword=models.CharField(max_length=25)
    nemail=models.CharField(max_length=25)

class nusleave(models.Model):
    from_name=models.CharField(max_length=200)
    from_date=models.CharField(max_length=200)
    to_date=models.CharField(max_length=200)
    idate=models.CharField(max_length=200) 
    reason=models.CharField(max_length=200) 

class nuatt(models.Model):
    drname=models.CharField(max_length=200)
    drmail=models.CharField(max_length=200)
    drdate=models.CharField(max_length=200)
    drstatus=models.CharField(max_length=200)
    drcomment=models.CharField(max_length=200)



class accp(models.Model):
    acstatus=models.CharField(max_length=200)
    acreason=models.CharField(max_length=200)
    acdate=models.CharField(max_length=200)

class userreg(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)

class regcomp(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('declained','Declained'),
    ]
    rarea=models.CharField(max_length=25)
    remail=models.CharField(max_length=25)
    rcomp=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')



class userre(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)


class regcom(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('declained','Declained'),
    ]
    rarea=models.CharField(max_length=25)
    remail=models.CharField(max_length=25)
    rcomp=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    

   
   
   

