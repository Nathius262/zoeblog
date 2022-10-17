from asyncio import protocols
import site
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .views import home_screen_view

class HomeStaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return['home_screen_view',]

    def location(self, item):
        return reverse('home')