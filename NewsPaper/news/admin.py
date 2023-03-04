from django.contrib import admin
from .models import *
from django.contrib.admin import TabularInline, StackedInline


class PostCategoryAdmin(TabularInline):
    model = PostCategory
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryAdmin]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(SubscribersCategory)
