from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
# Create your views here.


class ListExampleWorksView(TemplateView):
    template_name = "exampleworks/list.html"
