import login.models as models
import requests
from django.http import HttpResponse

def check_user(request):

    if request.method == "GET":
