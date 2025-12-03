from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from user.models import User


# Create your views here.
def home(request):
    user = User.objects.filter(username="default").first()
    context = {'user': user}
    return render(request, "../templates/home.html", context)

