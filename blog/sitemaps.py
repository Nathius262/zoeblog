from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq =  "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date_updated

    def location(self, obj):
        return obj.get_absolute_url()