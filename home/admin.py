from django.contrib import admin

from .models import Product, Coupon

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id','name','price','status')
#
# admin.site.register(Product,ProductAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status')
    list_filter = ('id','name','status')
    list_editable = ('name','price')
    list_per_page = 25


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id','product','coupon_code','description','discounted_price')