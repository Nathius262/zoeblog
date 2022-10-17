from django.contrib.sitemaps import Sitemap
from .models import Account

class AccountSitemap(Sitemap):
    changefreq =  "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Account.objects.all()

    def lastmod(self, obj):
        return obj.date_joined

    def location(self, obj):
        return obj.get_absolute_url()