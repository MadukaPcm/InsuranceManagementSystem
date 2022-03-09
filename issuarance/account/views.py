from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#homepage function 
def HomepageView(request):

    context = {}
    return render(request, 'index.html',context)

def AboutView(request):

    context = {}
    return render(request, 'homepages/about.html',context)

def InsuranceView(request):

    context = {}
    return render(request, 'homepages/insuranceplan.html',context)



def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = authenticate(request,username=username,password=password)
    
        if user is not None:
            if user.is_active:
                login(request,user)

                if request.user.is_superuser ==1:
                    return redirect('../admin/')
                else:
                    return redirect('dashboardissueraccounts_url')
            else:
                messages.info(request,'Ur account is blocked')
                return redirect('login_url')
        else:
            messages.info(request,'Ur None a member.')
            return redirect('login_url')

    context = {}
    return render(request, 'account/login.html', context)

def RegisterView(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')

        if User.objects.filter(username=request.POST['Username']).exists():
            messages.info(request,'useername already taken.')
            return redirect('register_url')
        
        if User.objects.filter(email=request.POST['Email']).exists():
            messages.info(request,'email already taken.')
            return redirect('register_url')

        if password1 != password2:
            messages.info(request,'password does not match')
            return redirect('register_url')

        if len(password1) != 8:
            messages.info(request, 'password, write 8 mixed characters')
            return redirect('register_url')
        else:
            ddatta = User.objects.create_user(username=username,email=email,password=password1)
            ddatta.first_name = first_name
            ddatta.last_name = last_name
            ddatta.save()

            return redirect('login_url')

    context = {}
    return render(request,'account/register.html', context)

def ForgotPasswordView(request):

    context = {}
    return render(request,'account/forgotpassword.html', context)

def SignoutView(request):

     logout(request)
     return redirect('homepage_url')