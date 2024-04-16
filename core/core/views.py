from django.http import HttpResponse
from django.shortcuts import render
from results.models import queries

def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('query')
        date = request.POST.get('date')
    
        if name and email and subject and description:
            # All fields are filled, proceed with saving the data
            data = queries(name=name, email=email, subject=subject, description=description, date=date)
            data.save()
            return HttpResponse("Form submitted successfully")
        else:
            # Some required fields are missing, handle the error (e.g., render the form again with error messages)
            return HttpResponse("Some required fields are missing")
       
        
       
        
    return render(request,'contact.html')


