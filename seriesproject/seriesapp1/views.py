from django.http import HttpResponse
from . models import seriestab
from django.shortcuts import render, redirect
from . forms import seriesform

# Create your views here.
def index(request):
    series=seriestab.objects.all()
    context={
        'series':series
    }
    return render(request,'index.html',context)
# def detail(request,series_id):
#     return HttpResponse("serial number is %s" % series_id)
def detail(request,series_id):
    series=seriestab.objects.get(id=series_id)
    context={
        'series':series
    }
    return render(request,'detail.html',context)
def add_series(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['image']
        seriese=seriestab(name=name,description=desc,year=year,image=img)
        seriese.save()
    return render(request,'add.html')
def update(request,id):
    series=seriestab.objects.get(id=id)
    form=seriesform(request.POST or None,request.FILES,instance=series)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'series':series})
def delete(request,id):
    if request.method=="POST":
        series=seriestab.objects.get(id=id)
        series.delete()
        return redirect('/')
    return render(request,'delete.html')
