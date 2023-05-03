from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=topicform()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data is submitted successfully')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)