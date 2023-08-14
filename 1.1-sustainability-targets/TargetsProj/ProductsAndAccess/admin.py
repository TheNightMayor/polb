from django.contrib import admin

from .models import Route, Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
    list_display = ["Product_Name"]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": (tuple(["Product_Name", "Product_Type"]),"Description", "Media"),}),)
    search_fields = ["Product_Name"]
    list_display = ["Product_Name", "Product_Type"]


class RouteAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['Title', 'Description', 'Origin', 'Destination']})]
    search_fields = ['Origin', 'Destination']
    list_display = ['Title', 'Origin', 'Destination']
    inlines = [ProductInline]
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Route, RouteAdmin)
# Register your models here.
