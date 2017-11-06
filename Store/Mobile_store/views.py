from django.shortcuts import render, redirect

# Create your views here.
from Mobile_store.models import Brand,Mobiles
from rest_framework.decorators import api_view
from .serializers import Brand_serializers, Mobiles_serializers
from rest_framework.response import Response
from .forms import brandForm, mobilesForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect

def home(request):

	brands = Brand.objects.all()
	return render (request, 'index.html', {'brands':brands})

@api_view(['GET','POST'])
def get_brands(request):
	print("test")
	if request.method=='POST':
		print(request.POST)
		brand = Brand.objects.get(id=request.POST['id'])
		models = Mobiles.objects.get(brand_id=brand)
		serializer = Mobiles_serializers(models)
		return Response(serializer.data)
	if request.method =='GET':
		models = Brand.objects.all()
		serializer = Brand_serializers(models,many=True)
		return Response(serializer.data)

def add_brand(request):
	if request.method=="POST":
		form = brandForm(request.FILES)
		if form.is_valid:
			form.save()
		return redirect ('/')

	else:
		form = brandForm()
		return render(request, 'add.html', {'form':form})

@api_view(['POST','GET'])
def add_mobiles(request):
	if request.method == 'POST':
		form = mobilesForm(request.POST,request.FILES)
		if form.is_valid:
			form.save()
			models = Mobiles.objects.all()
			serializer = Mobiles_serializers(models,many=True)
			return Response(serializer.data)
		
	else:
		form = mobilesForm()
		return render(request,'add_mobiles.html',{'form':form})



@api_view(['POST','GET'])
def get_mobiles(request):
	models = Mobiles.objects.all()
	serializer = Mobiles_serializers(models,many=True)
	return Response(serializer.data)

def view_mobiles(request):
	return render(request, 'misc.html',{})

@api_view(['GET','POST'])
def update_mobiles(request, id):
	if request.method == 'POST':
		inst = Mobiles.objects.get(id=id)
		form = mobilesForm(request.POST,request.FILES,instance=inst)
		if form.is_valid:
			form.save()
			return Response({'status':'success'})
	
	else:
		inst=Mobiles.objects.get(id=id)
		form=mobilesForm(instance=inst)
		return render(request, 'add_mobiles.html', {'form':form})

@api_view(['GET'])
def delete_mobiles(request, id):
	inst = Mobiles.objects.get(id=id)
	inst.delete()
	return redirect('/view_mobiles/')
