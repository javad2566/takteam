from django.contrib.sitemaps import Sitemap
from courses.models import Course
from django.urls import reverse

class CourseSingleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Course.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('courses:detail_courses',kwargs={"id":item.id})
    





class CoursesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ["courses:list_courses",]

    def location(self, item):
        return reverse(item)