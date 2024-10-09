from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class AccountsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["accounts:register","accounts:profile","accounts:login","accounts:logout","accounts:code"]

    def location(self, item):
        return reverse(item)