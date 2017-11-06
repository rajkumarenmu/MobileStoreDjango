from django.contrib import admin

# Register your models here.
from Mobile_store.models import Brand, Mobiles

class BrandAdmin(admin.ModelAdmin):
	list_display = ["brand_name", "country"]
	class Meta:
		model = Brand
		

class MobilesAdmin(admin.ModelAdmin):
	list_display = ["brand_id", "model_no", "price"]
	class Meta:
		model = Mobiles
		

admin.site.register(Brand, BrandAdmin)
admin.site.register(Mobiles, MobilesAdmin)