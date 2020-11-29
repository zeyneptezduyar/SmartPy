from django.shortcuts import render, redirect
from django.contrib import messages

from .smartly import *

def register(request):
    if request.method == 'POST':

        res = request.POST['input']

        title = HaikalFunction(res)

        context = {
            'title': res,
        }
        return render(request, 'back/showquiz.html', context)
       
    else:
        context = {
            'title': "SmartPy"
        }
        return render(request, 'back/register.html', context)



def HaikalFunction( s ):
    return "hello"
       

