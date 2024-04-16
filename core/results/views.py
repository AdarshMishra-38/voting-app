from django.shortcuts import render
from polls.models import pollresult
import json


# Create your views here.

def show_view(request):
    
    infos = request.session.get('form_data')
    data_from_db = pollresult.objects.all()
    data_as_json = json.dumps(list(data_from_db.values()))
    
    return render(request, 'results.html',{'infos':infos, 'data_as_json':data_as_json})
