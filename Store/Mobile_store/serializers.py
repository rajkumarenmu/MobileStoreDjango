from .models import Brand, Mobiles
from rest_framework import serializers

class Brand_serializers(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ['brand_name', 'country']

class Mobiles_serializers(serializers.ModelSerializer):
	#brand_id = Brand_serializers(many=True)
	class Meta:
		model = Mobiles
		fields = ['id','model_no', 'price','description','image', 'brand_id']