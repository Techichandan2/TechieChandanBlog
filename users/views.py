
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Message
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from blog.views import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confPassword = request.POST['cpassword']
        # checks and validation
        if len(first_name) < 2:
            messages.warning(request, 'First name must be at least 2 characters')
            return redirect('register')
        
        if len(first_name)>15:
            messages.warning(request, 'First name should only contain 15 characters')
            return redirect('register')
        
        if len(last_name) < 2:
            messages.warning(request, 'Last name must be at least 2 characters')
            return redirect('register')
        
        if len(last_name) > 15:
            messages.warning(request, 'Last name should only contain 15 characters')
            return redirect('register')
        
        if ((not first_name.isalpha()) or first_name.isnumeric()):
            messages.warning(request, 'First name should only contains characters')
            return redirect('register')
        
        if ((not last_name.isalnum()) or last_name.isnumeric()):
            messages.warning(request, 'Last name should only contains characters')
            return redirect('register')
        
        if (not password.isalnum()):
            messages.warning(request, 'Password must contain characters and numbers')
            return redirect('register')
        
        if len(password) < 8:
            messages.warning(request, 'Password must be at least 8 characters')
            return redirect('register')
        
        if len(password) > 15:
            messages.warning(request, 'Password should only contains maximum 15 characters')
            return redirect('register')
        
        if(password != confPassword):
            messages.warning(request, 'Password does not match')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'The username already exists, please choose another username')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'The email already used, please try again with another email')
            return redirect('register')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save();
        
        messages.success(request,'You have successfully registered')
        return redirect('login')
    
    return render(request, 'users/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticating user credentials
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password, please try again later')
            return redirect('login')
        
    return render(request, 'users/login.html')


def Logout(request):
    logout(request)
    return redirect('home')


def ChangePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_pass = request.POST['currentPass']
            new_pass = request.POST['newPass']
            conf_New_pass = request.POST['confNewPass']
            
            # checks and validation
            if len(new_pass) <8:
                messages.warning(request,'Password should be at least 8 characters')
                return redirect('changepass')
            
            if len(new_pass) > 15:
                messages.warning(request,'Password should only contains maximum 15 characters')
                return redirect('changepass')
            
            if (not new_pass.isalnum()):
                messages.warning(request, 'Password must contain characters and numbers')
                return redirect('changepass')
            
            if new_pass != conf_New_pass:
                messages.warning(request, 'Password does not match, please try again')
                return redirect('changepass')
                
            
            usr = authenticate(username=request.user.username,password = current_pass)
            usr.set_password(new_pass)
            usr.save()
            messages.success(request,'Password Changed Successfuly')
            logout(request)
            return redirect('login')
            
        return render(request, 'users/changepass.html')
    else:
        return redirect('login')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        #checks and validation
        if len(name)<4:
            messages.warning(request, 'Name must contains at least 4 characters')
            return redirect('contact')
            
        if len(name)>15:
            messages.warning(request, 'Name should only contains maximum 15 characters')
            return redirect('contact')
        
        if name.isalnum():
            messages.error(request, 'Name should only contain latters')
            return redirect('contact')
        
        
        if len(email)>100:
            messages.error(request, 'Email should only contains 100 characters')
            return redirect('contact')
            
        if len(message)>250:
            messages.warning(request, 'Message should only contain 250 characters')
            return redirect('contact')

        contact = Message(
            Name = name,
            Email = email,
            Message = message
        )
        contact.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')
        
    return render(request, 'users/contact.html')



    