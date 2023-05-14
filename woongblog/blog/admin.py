from django.contrib import admin

# Register your models here.
from .models import Post, Category

# admin 페이지 검색창
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)