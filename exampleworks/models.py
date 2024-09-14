from django.db import models

# Create your models here.



class Work(models.Model):
    title= models.CharField(max_length=255,verbose_name="عنوان کار")
    image = models.ImageField(upload_to="works/",null=True,blank=True,verbose_name="عکس کار")
    discription = models.TextField(verbose_name="توضیحات")
    discription2 = models.TextField(null=True,blank=True,verbose_name="توضیحات 2 ")
    address = models.TextField(null=True,blank=True,verbose_name="ادرس سایت ")
    director = models.TextField(verbose_name="مجری طرح")
    category = models.ManyToManyField('Category')
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ["created_date"]
        verbose_name = "نمونه کار"
        verbose_name_plural = " نمونه کار ها "    
    



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها" 
        