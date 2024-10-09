from django.db import models
from jalali_date import datetime2jalali,date2jalali

from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to="courses/")
    discription  = models.TextField()
    status = models.BooleanField(default=True)
    price = models.BigIntegerField(default=0)
    price_percented = models.BigIntegerField(default=0)
    free = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    teacher = models.TextField()
    category = models.ManyToManyField('Category')
    student = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["created_date"]
        verbose_name = "دوره "
        verbose_name_plural = "دوره ها "    
    
    def Created_at(self):
        return date2jalali(self.created_date)



    def get_absolute_url(self):
        return reverse('courses:detail_courses',kwargs={"id":self.id})


class Category(models.Model):
    name = models.CharField(max_length=255)
    discription  = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها" 
        




        
class Comment(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    message = models.TextField()
    email = models.EmailField()
    allow = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    
    
    
    class Meta:
        verbose_name = "گامنت"
        verbose_name_plural = "کامنت ها "


    def Created_at(self):
        return date2jalali(self.created_date)



