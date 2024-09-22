from django.db import models
from jalali_date import datetime2jalali



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
        return datetime2jalali(self.created_at)



class Category(models.Model):
    name = models.CharField(max_length=255)
    discription  = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها" 
        