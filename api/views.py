from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,JsonResponse
from django.forms.models import model_to_dict
from api.models import ProductModel
import json

def get_all(request):
    if request.method =='GET':
        products = ProductModel.objects.all()
        pro_json = [model_to_dict(products) for products in products]
        return  JsonResponse(pro_json,safe=False)

def get_by_id(requset,pk):
    try:
        product = ProductModel.objects.get(id = pk)
    except ProductModel.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    if requset.method =='GET':
        return JsonResponse(model_to_dict(product))

def create(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
      
        product = ProductModel.objects.create(
            name= data.get('name'),
            price= data.get('price'),
            quantity= data.get('quantity'),
            description= data.get('description')
        )
        return JsonResponse(model_to_dict(product))

def update(request,pk):
    try:
        product = ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    if request.method =='PUT':
        data = json.loads(request.body.decode('utf-8'))
        product.name = data.get('name',product.name)
        product.price = data.get('price',product.price)
        product.quantity = data.get('quantity',product.quantity)
        product.description = data.get('description',product.description)
        product.save()
        return  JsonResponse(model_to_dict(product))    
def delete(request,pk):
    try:
        product = ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    if request.method =='DELETE':
        product.delete()
        return JsonResponse({'deleted':True},safe=False)
        
def lookname(request,str):
    if request.method =='GET':
        products = ProductModel.objects.filter(name__icontains=str)
        pro_json = [model_to_dict(product) for product in products]
        return  JsonResponse(pro_json,safe=False)

def lookgt(request,pk):
    if request.method =='GET':
        products = ProductModel.objects.filter(price__gt=pk)
        pro_json = [model_to_dict(product) for product in products]
        return  JsonResponse(pro_json,safe=False)
def looklte(request,pk):
    if request.method =='GET':
        products = ProductModel.objects.filter(price__lte=pk)
        pro_json = [model_to_dict(product) for product in products]
        return  JsonResponse(pro_json,safe=False)
    
def lookrange(request,min,max):
    if request.method =='GET':
        products = ProductModel.objects.filter(price__range=(min,max))
        pro_json = [model_to_dict(product) for product in products]
        return  JsonResponse(pro_json,safe=False)
    