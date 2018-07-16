from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .fusioncharts import FusionCharts
from tmsapp.models import trafficAtA,trafficAtB,trafficAtC,trafficAtD
import math
import paho.mqtt.client as mqtt
# renders landing page
def loginpage(request):
    return render(request,'loginpage.html',{})
# server function for login
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/main/')
        else:
            stats='Unauthorized'
            return render(request,'loginpage.html',{'stats':stats})
#         main page function, access restricted by login decorators
@login_required(login_url='/loginpage/')
def main(request):
#     ordering data in for of ids
    DATA=trafficAtA.objects.all().order_by('id')
    DATA1=trafficAtB.objects.all().order_by('id')
    DATA2=trafficAtC.objects.all().order_by('id')
    DATA3=trafficAtD.objects.all().order_by('id')
#     extracting last updated values in the data base
    DATAREV=DATA.reverse()[:1]
    for k in DATAREV:
        a=math.floor(k.Trafficdensity)
    DATAREV1= DATA1.reverse()[:1]
    for k in DATAREV1:
        l=math.floor(k.Trafficdensity)
    DATAREV2= DATA2.reverse()[:1]
    for k in DATAREV2:
        c=math.floor(k.Trafficdensity)
    DATAREV3= DATA3.reverse()[:1]
    for k in DATAREV3:
        d=math.floor(k.Trafficdensity)
    return render(request, 'main.html', {'a':a,'l':l,'c':c,'d':d})
# server function for logout
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/loginpage/')
@login_required(login_url='/loginpage/')
def manualoveride(request):
    return render(request,'manualoveride.html',{})
# @login_required(login_url='/loginpage/')
def automate(request):
    broker_address = "172.16.73.4"
    # broker_address="iot.eclipse.org"
    print("creating new instance")
    client = mqtt.Client("P1")  # create new instance
    print("connecting to broker")
    client.connect(broker_address)  # connect to broker
    DATA = trafficAtA.objects.all().order_by('id')
    DATA1 = trafficAtB.objects.all().order_by('id')
    DATA2 = trafficAtC.objects.all().order_by('id')
    DATA3 = trafficAtD.objects.all().order_by('id')
    DATAREV = DATA.reverse()[:1]
    for k in DATAREV:
        a = math.floor(k.Trafficdensity)
    DATAREV1 = DATA1.reverse()[:1]
    for k in DATAREV1:
        l = math.floor(k.Trafficdensity)
    DATAREV2 = DATA2.reverse()[:1]
    for k in DATAREV2:
        c = math.floor(k.Trafficdensity)
    DATAREV3 = DATA3.reverse()[:1]
    for k in DATAREV3:
         d = math.floor(k.Trafficdensity)
    client.loop_start()  # start the loo
    print("Publishing message to topic", "Signal")
#     checking which opposite pairs of junction has high traffic
    if (a + c) > (l + d):
        client.publish("SignalAtAGreen/", "A")
    elif (l + d) > (a + c):
        client.publish("SignalAtAGreen/", "B")
    else:
        client.publish("SignalAtAGreen/", "0")
    return HttpResponse("Automated for a Single instance");
