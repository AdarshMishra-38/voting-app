from django.shortcuts import render,redirect
# from results.models import show_result
from .models import pollresult
from django.http import HttpResponse
# from .forms import VoteForm


def show_vote_form(request):
    passed_data = request.session.get('form_data')
    

    return render(request, 'votepage.html', {'passed_data': passed_data})  
  
  
def save_to_db(request):
    if request.method == 'POST':
        form_name = request.POST.get('name')
        form_age = request.POST.get('age')
        form_district = request.POST.get('district')
        form_choice = request.POST.get('votefor')
        data = pollresult(name=form_name, age=form_age, district=form_district, choice=form_choice)
        
        data.save()
        return HttpResponse(f"saving data successful")
        
          # return HttpResponse(f"saving data unsuccessful")
          
        
    return HttpResponse(f"hi")
     
   

