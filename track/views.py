from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('hello from track app')
def alltracks(request):
    # return HttpResponse('alltracks')
    return render(request,'list.html')
def trackbyid(request,id):
    # return HttpResponse(f'trackbyid{id}')
    return  render(request,'showtrack.html')
def trackbyname(request,name):
    return HttpResponse(f'trackbyname{name}')
def trackupdate(request,id):
    return HttpResponse(f'trackupdate{id}')
def trackdelete(request,id):
    return HttpResponse(f'trackdelete{id}')


