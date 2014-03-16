from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from manager.models import Coach
import json

class JsonResponse(HttpResponse):
    def __init__(self,
                 content={}, 
                 mimetype=None,
                 status=None,
                 content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content),
                                           mimetype=mimetype,
                                           status=status,
                                           content_type=content_type)

def home(request):
    return render_to_response('manager/home/home.html', RequestContext(request))

def coach_page(request):
    coach_list = Coach.objects.all().order_by('-name')
    return render_to_response('manager/coach/list.html', RequestContext(request, {'coach_list': coach_list}))

def coach_list(request):
    coach_list = Coach.objects.all().order_by('-name')
    result = {}
    result['coach_list'] = [obj.to_json() for obj in coach_list]
    return JsonResponse(result, mimetype="application/json")

