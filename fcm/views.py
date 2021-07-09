from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


#fungsi-fungsi terkait data latih
#
#################################


def index_data_latih(request):
	return render (request, 'data-latih/index.html')