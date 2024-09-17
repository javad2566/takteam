from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Service
# Create your views here.
from django.views.generic.detail import DetailView
from django.contrib import messages


class ServicesListView(TemplateView):
    template_name = "services/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time_now = timezone.now()
        services = Service.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
        context["services"] = services
        return context


def service_datail_view(request,id):
    time_now = timezone.now()
    posts = Service.objects.exclude(published_date__gt=time_now).filter(status=True)
    service_single = get_object_or_404(posts,id=id)

    return render(request,"services/detail.html",{"service":service_single})



def order_work_register_view(request):
    if not request.user.is_authenticated:
        messages.error(request,"برای ثبت پروژه وارد حساب کاربری خود شوید")
        return render(request,"services/order_register.html")

    return render(request,"services/order_register.html")
