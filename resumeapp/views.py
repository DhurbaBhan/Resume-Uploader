from django.shortcuts import redirect, render,HttpResponse
from resumeapp.forms import UserRegistrationForm,UserLoginForm,ResumeForm
from resumeapp.models import AppUser,Resume
from django.views import View


# Create your views here.
def register(request):
    template='register.html'
    user_form=UserRegistrationForm
    context={'form':user_form}
    
    if request.method=='POST':
        obj=AppUser()
        obj.first_name=request.POST.get('first_name')
        obj.middle_name=request.POST.get('middle_name')
        obj.last_name=request.POST.get('last_name')
        obj.contact=request.POST.get('contact')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.save()
        context.setdefault('success','Account registered successfully..')
       
        return render (request,template,context)
    else:
        return render (request,template,context)  


def user_login(request):
    form=UserLoginForm
    if request.method=='POST':
        try:
            users=AppUser.objects.get(email=request.POST.get('email'))
            if request.POST.get('password')==users.password:
                template='dashboard.html'
                form=ResumeForm
                # storing session with session key 'session_email'
                request.session['session_email']=users.email
                # checking session key value
                if request.session.has_key('session_email'):
                    # accessing session data
                    
                    # context={'success_msg':'Welcome  ' +  request.session['session_email'],'form':form}
                    return redirect('home')

                else:  
                    template='login.html'  
                    context={'form':form,'error_msg':'Access denied'}
                    return render (request,template,context)

            else:
                context={'form':form ,'error_msg':'Invalid Email or Password'}
                template='login.html'
                return render (request,template,context)
        except:
            context={'form':form ,'error_msg':'Not registered yet.'}
            template='login.html'
            return render (request,template,context)

    else:
        context={'form':form}
        template='login.html'
        return render (request,template,context) 
def logout(request):
    if request.session.has_key('session_email'):
        # destroying the session in order to logout user from the system
        del request.session['session_email']
        template='login.html'
        user_form=UserLoginForm
        context={'form':user_form,'msg':'You are logged out successfully'}  
        return render(request,template,context)   
def dashboard(request):
    if request.session.has_key('session_email'):
        return render(request,'dashboard.html')

    else:
        form=UserLoginForm
        template='login.html'  
        context={'form':form,'error_msg':'Access Denied'}
        return render (request,template,context)

class HomeView(View):
    def get(self,request):
        form=ResumeForm
        users=Resume.objects.all()

        if request.session.has_key('session_email'):
            return render(request,'dashboard.html',{'users':users,'form':form}) 
        else:
            form=UserLoginForm
            template='login.html'  
            context={'form':form,'error_msg':'Access Denied'}
            return render (request,template,context)           

    def post(self,request):
        # form=ResumeForm()
        # r=Resume()
        # r.name=request.POST.get('name')
        # r.dob=request.POST.get('dob')
        # r.gender=request.POST.get('gender')
        # r.city=request.POST.get('city')
        # r.pin=request.POST.get('pin')
        # r.province=request.POST.get('province')
        # r.mobile=request.POST.get('mobile')
        # r.email=request.POST.get('email')
        # r.job_city=request.POST.get('job_city')
        # r.profile_image=request.POST.get('profile')
        # r.my_file=request.POST.get('my_file')
        # r.save()
        # return render(request,'dashboard.html',{'form':form})
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 

            form=ResumeForm() 
            users=Resume.objects.all() 
            return render(request,'dashboard.html',{'users':users,'form':form,'msgg': 'Your resume details have been saved successfully.'})
        else:
            
            context={'msg':'Your form is not valid.','form':form}
            return render(request,'dashboard.html',context) 
def user(request,idd):
    user=Resume.objects.get(id=idd)
    return render(request,'candidate.html',{'user':user})