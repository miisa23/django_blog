from django.contrib import admin
from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'views', 'author', 'category', 'img_preview']
    list_display_links = ['pk', 'title']
    list_editable = ['author', 'category']
    readonly_fields = ['views']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'created_at', 'article']
    list_display_links = ['article']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)

