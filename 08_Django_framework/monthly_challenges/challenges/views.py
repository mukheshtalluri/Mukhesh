from calendar import month

from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

health_challenges = {
    "january": "Drink at least 2 liters of water daily",
    "february": "Walk 10,000 steps every day",
    "march": "Eat at least 5 servings of vegetables daily",
    "april": "Practice 10 minutes of meditation daily",
    "may": "Do a 30-day body weight workout challenge",
    "june": "Limit screen time to 2 hours outside of work",
    "july": "Sleep at least 7 hours every night",
    "august": "Try a new healthy recipe every week",
    "september": "Reduce sugar intake by 50%",
    "october": "Stretch for 10 minutes every morning",
    "november": "Take the stairs instead of the elevator",
    "december": None
}


# Create your views here.
def monthly_challenges(request, month):
    try:
        challenge_text = health_challenges[month]
        return render(request,"challenges/challenge.html",{"text" : challenge_text, "month" : month} )
    except:
        raise Http404()

def month_redirect(request, month):
    months = list(health_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not found please select a month between 1 to 12.")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def index(request):
    months = list(health_challenges.keys())
    return render(request, 'challenges/index.html', {'months' : months})

