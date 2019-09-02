from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.


def list(request):
    url = "https://api.github.com/events"
    response = requests.get(url).json()
    context = {
        "results" : response,
    }
    return render(request,'list.html', context)
    # return JsonResponse(response, safe=False)


def detail(request):
    url = request.GET.get("detail")
    response = requests.get(url).json()

 


    context = {
    "r" : response,
    }

    return render(request,'detail.html', context)