from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from app.models import Item
from api.items_serializer import ItemSerializer
from rest_framework.renderers import JSONRenderer
import requests
import json


# Create View from Rest Api As simple way
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    items = ItemSerializer( Item.objects.all(),many=True)

    return Response(items.data)

# Create View from Rest APi AS Best practice code
# Insider REST API
@permission_classes((permissions.AllowAny,))
class ItemsList(APIView):
    def get(self,request):
        items = ItemSerializer( Item.objects.all(),many=True)
        
        return Response(items.data)
    
    def post(self,request):
                   
        items = ItemSerializer( Item.objects.all(),many=True)

        return Response(items.data)
    
    
# Outsider API
@permission_classes((permissions.AllowAny,))
class OutAPIData(APIView):
    def get(self,request):
        items= requests.get("https://jsonplaceholder.typicode.com/users")
        return Response(items.json())
    
    def post(self,request):
           
        # items= requests.post("https://jsonplaceholder.typicode.com/users")
        items= requests.get("https://jsonplaceholder.typicode.com/users")

        return Response(items.json())
