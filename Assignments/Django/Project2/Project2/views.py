from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("<html><h1>Hello Students.</h1></html>")
def student_view(request):
    return render(request, "student.html")