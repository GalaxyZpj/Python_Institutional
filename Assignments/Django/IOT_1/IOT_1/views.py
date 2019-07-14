from django.shortcuts import render
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
import time

def remote_page(request):
    return render(request, "iot.html")
def iot_connect(request):
    btn = request.GET['btn']
    print(btn)
    connect(btn)
    return render(request, "iot.html")

def connect(s):
    pc=PNConfiguration()
    pc.subscribe_key="sub-c-88748fa0-9c8c-11e9-ab0f-d62d90a110cf"
    pc.publish_key="pub-c-9687c108-59d1-4d77-a4f7-289f64564b77"
    pc.ssl=True
    pubnub = PubNub(pc)
    # Listen for Messages on the Market Order Channel
    channel = 'lock'

    def show(msg,stat):
        if(msg and stat):print(msg.timetoken,stat.status_code)
        else:
            print("Error",stat and stat.status_code)
    pubnub.publish().channel(channel).message(s).pn_async(show)
    time.sleep(2)
