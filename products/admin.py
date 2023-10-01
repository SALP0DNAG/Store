from django.contrib import admin
from . import models

admin.site.register(models.ProductCategory)
admin.site.register(models.Basket)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = models.Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp', )
    extra = 0
