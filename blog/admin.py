from django.contrib import admin
from . import models
# Register your models here.

class ReplyInline(admin.TabularInline):
    model = models.reply
    extra = 1

class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]
    list_display = ('nick', 'content', 'time','public')
    list_filter = ['nick']
    search_fields = ['content']

class ReviewInline(admin.TabularInline):
    model = models.review
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ('article_id','title', 'time','public')
    list_filter = ['title']
    search_fields = ['content']



admin.site.register(models.admin_user)
admin.site.register(models.user)
admin.site.register(models.article, ArticleAdmin)
admin.site.register(models.review, ReviewAdmin)
admin.site.register(models.reply)