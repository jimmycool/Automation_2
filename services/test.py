'''
Created on 25-Mar-2023

@author: Dell
'''
from django.shortcuts import render

def index(request):
    return render(request, "index.html")