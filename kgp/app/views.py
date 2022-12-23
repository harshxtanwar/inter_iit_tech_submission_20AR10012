from typing import Collection
from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    he = {1 : "coming from backend"}
    ## NO backend code required here
    return render(request, 'home.html', {'hel':he})