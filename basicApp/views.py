# from django.contrib.sites import requests
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("hello world!")

@csrf_exempt
def add(request):
    url = "https://dummy.restapiexample.com/api/v1/create"
    payload = {"name": "test", "salary": "123", "age": "23"}
    response = requests.post(url, data=payload, headers={'content-type': 'json'})
    print(response)
    return HttpResponse("Data added!!")

def getById(request, pk):
    url = f'http://www.omdbapi.com/?i={pk}&apikey=d369cb8c'
    response = requests.get(url)
    print(response.url)
    if response.status_code == 200:
        return HttpResponse(response.text)
    else:
        return HttpResponse("There was a problem Because", response.reason)
