from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} {idade} anos!<h1>')

