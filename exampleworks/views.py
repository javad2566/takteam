from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from .models import Work,Category
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from courses.models import Category
from django.utils import timezone

class ListExampleWorksView(TemplateView):
    template_name = "exampleworks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time_now = timezone.now()
        works = Work.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
        context["all_works"] = works
        return context
    


def work_datail_view(request,id):
    time_now = timezone.now()
    categorys = Category.objects.all()

    works = Work.objects.exclude(published_date__gt=time_now).filter(status=True)
    work = get_object_or_404(works,id=id)
    work.counted_view +=1
    work.save()
    return render(request,"exampleworks/detail.html",{"work":work,"categorys":categorys})