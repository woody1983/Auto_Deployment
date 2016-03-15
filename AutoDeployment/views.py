from django.shortcuts import render
from django.shortcuts import render_to_response
from AutoDeployment.models import Deploy

# Create your views here.
# Create your views here

def index(request):
    RFC_list = Deploy.objects.all().order_by('-Deploy_Date') 
    return render_to_response('index.html',{'lists':RFC_list}) 

