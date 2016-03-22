from django.shortcuts import render
from django.shortcuts import render_to_response
from AutoDeployment.models import Deploy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
# Create your views here.
# Create your views here
now = datetime.datetime.now().strftime("%Y%m%d")
def index(request):
    RFC_list = Deploy.objects.all().order_by('-Deploy_Date')
    paginator = Paginator(RFC_list, 12)
    page = request.GET.get('page')
    try:
        RFC_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        RFC_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        RFC_list = paginator.page(paginator.num_pages)

    return render_to_response('index.html',{'lists':RFC_list})
