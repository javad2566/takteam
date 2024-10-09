from django.db import models
from jalali_date import datetime2jalali
# Create your models here.
class WorkField(models.Model):
    name = models.CharField(max_length=255)
    disctption = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = " زمینه فعالیت  "
        verbose_name_plural = "  زمینه فعالیت ها " 

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField(default=0)
    email = models.EmailField()
    work = models.ManyToManyField(WorkField)
    disctption = models.TextField()
    image = models.ImageField(upload_to="team/")
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ["created_date"]
        verbose_name = "عضو تیم "
        verbose_name_plural = "اعضای تیم "    
    
    def Created_at(self):
        return datetime2jalali(self.created_at)
    


class ContactUs(models.Model):
    title = models.CharField(max_length=255)
    phone = models.BigIntegerField(default=0)
    email = models.EmailField()
    disctption = models.TextField()
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)

    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["created_date"]
        verbose_name = " تیکت  "
        verbose_name_plural = "تیکت ها   "    
    
    def Created_at(self):
        return datetime2jalali(self.created_at)
    


class Subscribe(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ["created_date"]
        verbose_name = "دنبال کردن "
        verbose_name_plural = "دنبال کنندگان "    
    
    def Created_at(self):
        return datetime2jalali(self.created_date)