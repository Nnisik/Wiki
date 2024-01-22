from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def search(request):
    return render(request, 'wiki/search.html')

def index(request):
    return render(request, 'wiki/index.html', {
        "topic": "TOPIC",
    })