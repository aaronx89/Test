# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    context = {
    'title': 'Home',
    }

    template = 'index.html'
    return render(request,template,context)