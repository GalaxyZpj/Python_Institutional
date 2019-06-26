from django.http import HttpResponse
from django.shortcuts import render
def welcome(request):
    return HttpResponse('<html><h1>My First Django Script</h1></html>')
def calculator_view(request):
    return render(request, 'si.html', {'value': 'See Here'})
def calculate(request):
    amt = int(request.GET['amt'])
    rate = int(request.GET['rate'])
    time = int(request.GET['time'])
    si = (amt*rate*time)/100
    return render(request, 'si.html', {'value': si})
