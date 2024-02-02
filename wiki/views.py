from django.shortcuts import render
from django.http import HttpResponse
from django import forms


class SearchForm(forms.Form):
    q: forms.CharField(label="")

# Create your views here.
def search(request):
    return render(request, 'wiki/search.html', {
        "form": SearchForm(),
    })

def index(request, topic):
    return render(request, 'wiki/index.html', {
        "topic": topic,
    })