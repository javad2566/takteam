from typing import Any
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from .models import Work,Category
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

from django.utils import timezone

class ListExampleWorksView(TemplateView):
    template_name = "exampleworks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time_now = timezone.now()
        works = Work.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
        context["all_works"] = works
        return context
    


class SingleExampleWorkView(DetailView):
    model = Work
    pk_url_kwarg = "id"
    template_name = "exampleworks/detail.html"
    context_object_name = "work"