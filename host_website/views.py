from django.shortcuts import render
import requests

# Create your views here.
def host(request):
    api_url = "https://api.github.com/users/kamal63442/repos"
    response = requests.get(api_url)
    value = response.json()
    return render(request,'index.html', {'data':value})