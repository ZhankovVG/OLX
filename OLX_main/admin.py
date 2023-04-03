from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', )
    prepopulated_fields = {'url': ('name', )}


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'draft', 'get_poster', 'url', 'category')
    list_display_links = ('title', )
    list_filter = ('title', 'category__name')
    list_editable = ('draft', )
    inlines = [CommentsInline]

    def get_poster(self, objects):
        return mark_safe(f"<img src={objects.poster.url} width '50' ")

    prepopulated_fields = {'url': ('title', )}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'email')
    list_display_links = ('name', )
    readonly_fields = ('email', )
