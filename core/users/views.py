from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://localhost:8000/users/register/")
        else:
            form = UserCreationForm()
                
    return render(request, 'register.html', {"form": form})
    
