from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>Welcome Ji Welcome to the first DJANGO MANGO</h1>")

def entry(request):
    return render(request, '')
    # return HttpResponse("<h1>This the entry section for the usernames</h1>")