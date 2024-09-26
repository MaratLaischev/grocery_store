from django.contrib import admin

from category.models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0


class CategorieAdmin(admin.ModelAdmin):
    inlines = (
        SubCategoryInline,
    )
    list_display = (
        'id',
        'name',
        'slug',
        'image'
    )
    search_fields = ('name', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'parent',
        'name',
        'slug',
        'image'
    )
    search_fields = ('parent__name', 'name', 'slug')
    list_filter = ('parent__name', 'name')


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategorieAdmin)
