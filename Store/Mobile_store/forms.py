from .models import Brand, Mobiles
from django.forms import ModelForm


class brandForm(ModelForm):
	class Meta:
		model = Brand
		fields = ["brand_name", "country"]

class mobilesForm(ModelForm):
	class Meta:
		model = Mobiles
		fields = ["brand_id","model_no", "description", "price", "image", "weight", "ram", "internal_memory", "front_camera"]
