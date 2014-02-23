from django.template import RequestContext
from django.shortcuts import render_to_response
from manager.models import Coach

def coach_list(requst):
	coach_list = Coach.objects.all().order_by('-name')
	return render_to_response('manager/coach/list.html', RequestContext(requst, {'coach_list': coach_list}))
