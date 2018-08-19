from django.shortcuts import render
import asyncio

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)
