from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse()


def monthly_challenge_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if(month == "january"):
        challenge_text = "This works!"
    elif(month == "february"):
        challenge_text = "This is February!"
    elif(month == "march"):
        challenge_text = "Get ready for Baseball!"
    else:
        return HttpResponseNotFound("Input NOT supported!")
    return HttpResponse(challenge_text)
