from django.http import HttpResponse
from django.shortcuts import render 
import requests,json
def index(request):
    response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts").json()
    response2 = requests.get("https://my-json-server.typicode.com/typicode/demo/comments").json() 
    return render(request,"home.html",{"response":response,"response2":response2})
def index2(request):
    response=[]
    count=0
    v="https://reqres.in/api/users?page="
    for i in range(1,13):
        response+=[requests.get(v+str(i)).json()]
        b=response[i-1]["data"]
        if b != []:
            for j in range(0,len(b)):
              count+=1
    return render(request,"house.html",{"response":count})