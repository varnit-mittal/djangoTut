from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@csrf_protect
def login_view(request):
    context = {}
    if(request.method=="POST"):
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            context["success"]=True
            login(request,user)
            return redirect('/')
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        # user=authenticate(request,username=username,password=password)
        # if(user is None):
        #     context["error"]="Invalid username or password"
        # else:
    else:
        form=AuthenticationForm(request)
    context["form"]=form
    return render(request,'accounts/login.html',context=context)

def logout_view(request):
    context={}
    if(request.method=="POST"):
        logout(request)
        return redirect('/login')
    return render(request,'accounts/logout.html',context=context)

def register_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return redirect('/login')
    context={
        'form':form
    }

    return render(request,'accounts/register.html',context=context)