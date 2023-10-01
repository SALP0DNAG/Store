from django.contrib import admin
from . import models
from products.admin import BasketAdminInline


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
