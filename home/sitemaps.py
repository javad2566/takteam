from django.contrib.sitemaps import Sitemap
from courses.models import Course
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["home:index"]

    def location(self, item):
        return reverse(item)