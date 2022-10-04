from asyncio.windows_events import NULL
from audioop import reverse
from django.http import HttpRequest
from django.shortcuts import render, redirect
from discordoauth2 import models as dmodels
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.

main_adress = "http://localhost:8000"
main_page = "%s/main/home" %(main_adress)

def main_page(request: HttpRequest):
    users = dmodels.user_class.objects.all()
    context = {
        "user.id" : request.user.id,
        "user" : request.user
    }
    if request.user.is_authenticated:
        user = request.user.id
        user_object = dmodels.user_class.objects.get(id=user)
        return render(request,'main_logado.html', context)
    else:
        return render(request,'main_deslogado.html', context)

def log_out(request: HttpRequest):
    logout(request)
    return redirect(main_page)