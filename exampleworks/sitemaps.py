from django.contrib.sitemaps import Sitemap
from exampleworks.models import Work
from django.urls import reverse

class WorkSingleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Work.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('exampleworks:detail',kwargs={"id":item.id})
    





class WorksSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["exampleworks:list",]

    def location(self, item):
        return reverse(item)