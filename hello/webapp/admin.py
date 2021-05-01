from django.contrib import admin
from webapp.models import Product, Review

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'picture']
    list_filter = ['category']
    fields = ['name', 'description', 'category', 'picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'review', 'appraisal', 'moderated']
    fields = ['author', 'product', 'review', 'appraisal', 'moderated']


admin.site.register(Product, ProductsAdmin)
admin.site.register(Review, ReviewAdmin)


# Register your models here.
