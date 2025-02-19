from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<h1>hi im big c</h1> <p>rn its {now}</p>")

def screenprint(request):
    return render(request, "core/screenprint.html")

# add another thing for the black boooox