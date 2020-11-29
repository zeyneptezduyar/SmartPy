from django.shortcuts import render, redirect
from django.contrib import messages

from .smartly import *

def register(request):
    if request.method == 'POST':

        res = request.POST['input']

        title = get_word_and_definitions(res)

        context = {
            'questions': title,
        }
        return render(request, 'back/showquiz.html', context)
       
    else:
        context = {
            'title': "SmartPy"
        }
        return render(request, 'back/register.html', context)