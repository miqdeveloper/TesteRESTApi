from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework import response
from requests import request as rq
import json
from .models import *

# Sale;
# • Seller;
# • Purchase;
# • Buyer;

# • Stock;

get_data = rq(url="https://fakestoreapi.com/products", method='get')

class stock(APIView):
    # STOCK - nome do item, quantidade, id
    
    def get(self, request, pk=None, format=None):
        try:
            
            
            data = get_data.json()
            
            print(request.data)
            
            # print("YourRequest", request)      
            return response.Response(data=data, status=200)
        except Exception as err:
            return response.Response(status=400, data={"Nada encontrado..."})
    
    def post(self, request):
        data = {"message": "rota 2 ok"}
        return response.Response(data=data, status=200)
    
class stockIntem(APIView):
    # STOCK - nome do item, quantidade, id
    
    def get(self, request, num=None, format=None):
        try:
            
            data = get_data.json()
            data = data[num]
            return response.Response(status=200, data=data)
        
        except Exception as err:
            return response.Response(status=400, data={"Nada encontrado..."})
    
class sale(APIView):
    
    def post(self, request):
        try:
            # saleId = request.data
            obj = json.dumps(request.data)
            obj = json.loads(obj)
            
            data = get_data.json()            
            data = data[obj["SaleId"]]

            if obj["CUPOM"] == "MAGICO100":
                price_now = data['price']
                data['price'] = (price_now - 20)
            
            return response.Response(status=200, data=data)
        except Exception as err:
            return response.Response(status=400, data={"Nada encontrado..."})
        
        

class seller(APIView):
    def get(self, request, cpf=None):
        data_cpf = cpf
        return response.Response(status=200, data={"cpf": data_cpf})
    
class purchase(APIView):
    def get(self, request, idI=None):
        return response.Response(status=200, data={"id_Venda":  idI})
    
class buyer(APIView):
    def post(self, request):
        
        data_ = request.data
        return response.Response(status=200, data={"cnpj": data_})
    
    
class relatorio(APIView):
    
    pass