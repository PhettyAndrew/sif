from django.shortcuts import render, redirect
from . models import Management, Team, News, Donations, Support, GeneralInfo, ShowImages
from .forms import SupporterForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    infoIndex=GeneralInfo.objects.all
    context={
        'infoIndex':infoIndex
    }
    return render(request,'appSigtuna/index.html',context)

def team(request):
    infoTeam=Team.objects.all
    context={
        'infoTeam':infoTeam
    }
    return render(request,'appSigtuna/team.html',context)

def news(request):
    infoNews=News.objects.all
    context={
        'infoNews':infoNews
    }
    return render(request,'appSigtuna/news.html',context)

def gallery(request):
    infoGallery=ShowImages.objects.all()
    paginator = Paginator(infoGallery, 3)
    page = request.GET.get('page' ,1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context={
        'posts': posts
    }

    return render(request,'appSigtuna/gallery.html',context)

def supporter(request):
    formSupport=SupporterForm(request.POST or None, request.FILES or None)
    infoIndex = GeneralInfo.objects.all
    context = {
        'infoIndex': infoIndex
    }
    if formSupport.is_valid():
        formSupport.save()
        return render(request,'appSigtuna/index.html',context)
    return render(request, 'appSigtuna/index.html', {'formSupport':formSupport})