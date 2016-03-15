from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django ! ")
    #context          = {}
    #context['hello'] = 'Hello World!'
    #return render(request, 'hello.html', context)
