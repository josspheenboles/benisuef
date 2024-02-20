from django.shortcuts import render,reverse
from  django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def newtrack(request):
    if(request.method=='POST'):
        trackname=request.POST['trackname']
        # Track.objects.create(name=trackname)
        track=Track()
        track.name=trackname
        track.save()
    return render(request,'track/newtrack.html')
def hello(request):
    return HttpResponse('hello from track app')
def alltracks(request):
    # return HttpResponse('alltracks')
    tracks=Track.objects.all()
    context={'tracks':tracks}

    return render(request,'track/list.html',context)
def trackbyid(request,id):
    # return HttpResponse(f'trackbyid{id}')
    track=Track.objects.get(id=id)
    context={'track':track}
    return  render(request,'track/showtrack.html',context)
def trackbyname(request,name):
    return HttpResponse(f'trackbyname{name}')
def trackupdate(request,id):
    if(request.method=='POST'):
        Track.objects.filter(id=id).update(name=request.POST['trackname'])
        return HttpResponseRedirect(reverse('Tracks'))
    track=Track.objects.get(id=id)
    context={'track':track}
    return render(request,'track/updatetrack.html',context)
    # return HttpResponse(f'trackupdate{id}')
def trackdelete(request,id):
    return HttpResponse(f'trackdelete{id}')


