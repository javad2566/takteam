from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Service,OrderWork
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
    service_single.counted_view += 1 
    service_single.save()
    return render(request,"services/detail.html",{"service":service_single})



def order_work_register_view(request):
    if not request.user.is_authenticated:
        messages.error(request,"برای ثبت پروژه وارد حساب خود شوید")
        return render(request,"services/order_register.html")
    elif request.method == "POST":
        title =request.POST.get("title")
        work = request.POST.get("work")
        discription = request.POST.get("discription")
        if title and work and discription:
            print(title,work,discription)
            OrderWork.objects.create(title=title,discription=discription,user=request.user,work=work)
            messages.success(request,"سفارش شما ثبت شد .")
            return redirect("/")
        else:
            messages.error(request,"تمامی فیلدهارا پر کنید !")

    return render(request,"services/order_register.html")
