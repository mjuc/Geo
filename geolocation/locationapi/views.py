from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MyLocationView(APIView):
    permission_classes = (IsAuthenticated,)

    def mylocation(self,request):
        
        response= request.get('http://api.ipstack.com/json/')
        data = response.json()
        return render(request, 'core/home.html', {
            'ip': data['ip'],
            'country': data['country_name']
        })

class HomeView():

    def home(self,request):
        return(render(request,'index.html'))

class RegisterView():

    def register(self,request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})