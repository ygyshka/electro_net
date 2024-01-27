from django.contrib import admin
from django.utils.html import format_html
from rest_framework.reverse import reverse

from electro_net.models import Supplier, Product

# Register your models here.


@admin.register(Supplier)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'country', 'city', 'street',
                    'number_house', 'products', 'parent_supplier_link', 'level', 'time_created',
                    'debt_to_supplier',)
    exclude = ('level',)
    list_filter = ('country', 'city',)
    actions = ('clear_debt',)

    def parent_supplier_link(self, obj):
        if obj.parent_supplier:
            link = reverse("admin:electro_net_supplier_change", args=[obj.parent_supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.parent_supplier.title)
        else:
            return "-"
    parent_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt_to_supplier = 0
            obj.save()
        self.message_user(request, "Задолженность перед поставщиком очищена успешно.")

    clear_debt.short_description = "Очистить задолженность перед поставщиком"

    def save_model(self, request, obj, form, change):
        obj.level_up()
        super().save_model(request, obj, form, change)


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'date_created')
