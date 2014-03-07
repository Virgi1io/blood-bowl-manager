from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from manager.models import Coach

def home(request):
    return render_to_response('manager/home/home.html', RequestContext(request))

def coach_page(request):
    coach_list = Coach.objects.all().order_by('-name')
    return render_to_response('manager/coach/list.html', RequestContext(request, {'coach_list': coach_list}))

def coach_list(request):
    coach_list = Coach.objects.all().order_by('-name')
    result = [obj.to_json() for obj in coach_list]
    return HttpResponse(simplejson.dumps(result), mimetype="application/json")
