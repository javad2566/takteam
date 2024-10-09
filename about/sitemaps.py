from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class AboutSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["about:about"]

    def location(self, item):
        return reverse(item)