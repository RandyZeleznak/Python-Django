from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)


admin.site.register(Author, PostAdmin)
admin.site.register(Post)
admin.site.register(Tag)
