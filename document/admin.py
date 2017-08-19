from django.contrib import admin

# Register your models here.
from document import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "create_time")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "content", "create_time")


class UploadFileAdmin(admin.ModelAdmin):
    list_display = ("title", "my_file", )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.UploadFile, UploadFileAdmin)
