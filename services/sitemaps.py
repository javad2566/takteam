from django.contrib.sitemaps import Sitemap
from services.models import Service
from django.urls import reverse

class ServicesSingleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Service.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('services:detail_services',kwargs={"id":item.id})
    





class ServicesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["services:list_services","services:order-register"]

    def location(self, item):
        return reverse(item)