from urllib import request
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

discord_oauth2_link = "https://discord.com/api/oauth2/authorize?client_id=1004110449169678370&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"
discord_oauth2_link2 = "https://discord.com/api/oauth2/authorize?client_id=1004110449169678370&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Flogin%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"

main_adress = "http://localhost:8000"

login_redirect = "%s/login/oauth2/login/redirect" %(main_adress)

authenticated_redirect = "%s/main/home" %(main_adress)

# Create your views here.

@login_required(login_url="login/oauth2/login")
def get_authenticated_user(request: HttpRequest):
    user = request.user
    return JsonResponse({"teste"})

def discordlogin(request: HttpRequest):
    return redirect(discord_oauth2_link2)

def discordlogin_redirect(request: HttpRequest):
    code = request.GET.get('code')
    user = exchange_code(code)
    login_user = authenticate(request, user = user)
    login(request, login_user)
    return redirect(authenticated_redirect)

def exchange_code(code: str):
    data = {
        "client_id" : "1004110449169678370",
        "client_secret" : "wJTS0isWz1JIipdr-RoMVB-FPGxf0jKR",
        "grant_type" : "authorization_code",
        "code" : code,
        "redirect_uri" : login_redirect,
        "scope" : "identify"
    }
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'authorization' : 'Bearer %s' % access_token
    })
    user = response.json()
    return user
