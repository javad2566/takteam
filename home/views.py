from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
from django.utils import timezone
from exampleworks.models import Work
from services.models import Service
class HomePageView(TemplateView):
    template_name = "home/index.html"


    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        time_now = timezone.now()
        works = Work.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")[0:3]
        services = Service.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")[0:3]

        context["works_home_page"] = works
        context["services_home_page"]= services
        return context