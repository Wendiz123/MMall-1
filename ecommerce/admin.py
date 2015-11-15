from django.contrib import admin
from .models import *

admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'getPicture', 'category', 'brand', 'formatted_price']

    def formatted_price(self, obj):
        return 'Rp.'+"{:,}".format(obj.price)

    def getPicture(self, obj):
         if obj.picture == '':
            img = "http://placehold.it/100?text=No+Picture"
         else:
            img = "/media/"+str(obj.picture)

         return "<img src='%s' width='100px' />" % (img)

    getPicture.allow_tags = True
    getPicture.short_description = 'Picture'
    formatted_price.short_description = "Price"

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
