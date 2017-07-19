from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import pytz, datetime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=00
    if 'diary' not in request.session:
        request.session['diary']=[]
    request.session.modified = True
    return render (request,'gold/index.html')

def farm(request):
    gold = random.randint(10,21)
    
    activity ={
        'activity':"went to the farm! you found..",
        'gold': gold,
        'time' : strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    request.session['diary'].append(activity)
    request.session['gold']+= gold
    return redirect('/')

def cave(request):
    gold = random.randint(5,10)
    activity ={
        'activity':"went to the cave! you found..",
        'gold': gold,
        'time' : strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    request.session['diary'].append(activity)
    request.session['gold']+= gold
    return redirect('/')

def house(request):
    gold = random.randint(2,5)
     
    activity ={
        'activity':"went to the house! you found..",
        'gold': gold,
        'time' : strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    request.session['diary'].append(activity)
    request.session['gold']+= gold
    return redirect('/')

def casino(request):
    odds= random.randint(0,101)
    gold= random.randint(0,51)
    
    if odds > 70:
        activity ={
            'activity': "went to the casino you won..",
            'gold': gold,
            'time' : strftime("%Y-%m-%d %H:%M %p", gmtime()),
        }
        request.session['diary'].append(activity)
        request.session['gold']+= gold
    else:
        activity ={
            'activity': "went to the casino you lost..",
            'gold': gold,
            'time' : strftime("%Y-%m-%d %H:%M %p", gmtime()),
        }
        request.session['diary'].append(activity)
        request.session['gold']-= gold
    return redirect('/')

def clear(request):
    
    request.session['gold']= 00
    request.session['diary']=[]

    return redirect('/')