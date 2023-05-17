from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog.models import Category, Post

# google 검색 최적화를 위해 사이트 구조를 알려줌
class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at