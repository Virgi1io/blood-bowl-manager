from django.template import RequestContext
from django.shortcuts import render_to_response
from manager.models import Coach

def home(request):
    return render_to_response('manager/home/home.html', RequestContext(request))

def coach_list(request):
	coach_list = Coach.objects.all().order_by('-name')
	return render_to_response('manager/coach/list.html', RequestContext(request, {'coach_list': coach_list}))
