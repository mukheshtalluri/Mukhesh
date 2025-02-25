from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:month>', views.month_redirect),
    path('<str:month>', views.monthly_challenges, name="monthly_challenges")
]