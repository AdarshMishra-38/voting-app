from django.urls import path
from . import views


urlpatterns = [
    path('',views.show_vote_form),
    path('pollresult/',views.save_to_db),
    
   ]