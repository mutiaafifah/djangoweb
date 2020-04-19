from django.shortcuts import render
# from django import request
def index(request):
    return render(request, 'index.html')