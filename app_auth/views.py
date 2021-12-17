from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm


# Create your views here.

def login_blog(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data ['username']
            pwd=form.cleaned_data['pwd']
            user=authenticate(username=username , password=pwd)
            if user is not None :
                return redirect('articles:creer')
            else:
                messages.error(request,"Erreur d'authentification")
                return render(request,'app_auth/login.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid '
            return render(request,'app_auth/login.html',{'form':form})
    
    else:
        form=LoginForm()
        return render(request,'app_auth/login.html',{'form':form})
        
        
        