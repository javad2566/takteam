from django.db import models
from jalali_date import datetime2jalali
from accounts.models import User# Create your models here.



class Service(models.Model):
    title= models.CharField(max_length=255,verbose_name="عنوان ")
    discription = models.TextField(verbose_name="توضیحات")   
    status = models.BooleanField(default=False)
    director = models.TextField(null=True,blank=True,verbose_name="مجری طرح")
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = " خدمات  ها" 

  
    
    def Created_at(self):
        return datetime2jalali(self.created_at)
    

work = [
    ("طراحی سایت با جنگو ", "طراحی سایت با جنگو "),
    ("طراحی سایت با ورپرس ", "طراحی سایت با ورپرس "),
    ("طراحی گرافیکی با فتوشاپ ", "طراحی گرافیکی با فتوشاپ "),
   
]

class OrderWork(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    title= models.CharField(max_length=255,verbose_name="عنوان ")
    discription = models.TextField(verbose_name="توضیحات")
    work = models.CharField(max_length=255, choices=work, default=None)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "لیست سفارش ها" 

  
    
    def Created_at(self):
        return datetime2jalali(self.created_at)