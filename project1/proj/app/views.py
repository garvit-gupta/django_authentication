from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.template.context_processors import csrf
# Create your views here.
def home(request): 
    context={}
    return render(request,"home.html",context)

def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            if user.is_active:
                login(request, user) 
                print 'logged in'        
                return redirect('dashboard')
        print 'User not defined'
        return HttpResponse('Wrong username or password')
        #print 'Invalid form'
        print form.errors     
        #return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()     
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            instance.set_password(raw_password)
            instance.save()
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)        
                    return redirect('dashboard')
        return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})




def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.user.get_username()=='':
        context={'message':'Please log in first'}
        return render(request,'home.html',context)    
    # if request.user.is_anonymous:
    #     return redirect('/')
    return render(request,'dashboard.html')

@login_required
def logoutuser(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

# @login_required
# def passwordreset(request):
#     if request.method='POST':
#         return render(request,'pass_reset.html',{})
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('dashboard')
        else:
            return redirect('change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'change_password.html',args)

