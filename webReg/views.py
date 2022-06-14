from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method =='POST':
        print('hello everyone')
        return redirect('patientdetails')
    else:
        print('bye everyone')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       email=request.POST['email']
       password1=request.POST['password1']
       password2=request.POST['password2']

       if password1==password2:
           if User.objects.filter(username=username).exists():
               print('username taken')
               messages.info(request,'Username taken')
               return redirect('register')
               
           elif User.objects.filter(email=email).exists():    
               print('email taken')
               messages.info(request,'email taken')
               return redirect('register')
           else:   
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created ')
                messages.info(request,'user created ')
                messages.info(request,'username is'+username)

                return redirect('login')
       else:
            print('password not matching')
            messages.info(request,'password not matching ')
            return redirect('register')
    else: 
        return render(request,'register.html') 

    return render(request,'register.html')  
    


def PatDetails(request):
    return render(request,'patientsdetail.html')

def logon(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

    

        # for authentication wheter it is in db or not 
        user=auth.authenticate(username=username,password=password)


        # if user is None:
        #     messages.info(request,'Username not Present')
        #     messages.info(request,'Create New User')
        #     print("username not present")


        #     return redirect('/')

        if user is not None:
            auth.login(request,user)
            print("user is present",user.username)
           
            

            return redirect('patientdetails')


        else: 
            messages.info(request,'invalid credentials ') 
            messages.info(request,'check username ,password or make new entry  ') 
            print("inside user not present")

            return redirect('/') 




            
    else:
        return render(request,'index.html') 
   