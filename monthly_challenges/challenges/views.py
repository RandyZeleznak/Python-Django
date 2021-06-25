from typing import Reversible
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges)

   # for month in months:
   #     capitalized_month = month.capitalize()
   #     month_path = reverse("monthly-challenges", args=[month])
   #     list_items += f"<li> <a href =\"{month_path}\"> {capitalized_month} </a></li>"

   #     response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


monthly_challenges = {
    "january": "Happy New Year!",
    "february": None,
    "march": "Get ready for Baseball!",
    "april": "Start of Baseball",
    "may": "Rainy Rainy Rainy!",
    "june": "Getting warm!!",
    "july": "Happy Fourth!",
    "august": "Dog Days!",
    "september": "Get ready for Football!",
    "october": "Halloween",
    "november": "Happy Thanksgiving!",
    "december": "Merry Christmas"
}


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid Input")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
      #  response_data = f"<h1>{challenge_text}</h1>"
      #  response_data = render_to_string("challenges/challenge.html")
      #  return HttpResponse(response_data)
    except:
        raise Http404()
     #   response_data = render_to_string("404.html")
     #   return HttpResponse(response_data)
