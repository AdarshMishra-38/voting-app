from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def createpoll(request):
    if request.method =='POST':
        form_data = request.POST
        if form_data:
            request.session['form_data']= form_data
            # return redirect('VoteHere:show_vote_form')     
        
            return HttpResponse("Form submission successfull")
        else:
            return HttpResponse("form submission failed ")
        
    return render(request, 'createpoll.html')
