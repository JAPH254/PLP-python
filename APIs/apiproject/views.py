from django.shortcuts import render
import requests

def home(request):
        # API FETCHING
        response = requests.get('https://api.github.com/events')
        res = response.json()
        data = res[0]['id']
        return render(request, 'templates/index.html',{'data':data})