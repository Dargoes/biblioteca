from django.shortcuts import render, redirect
from django.db import connection

def index(request):
    return render(request, 'base.html')


