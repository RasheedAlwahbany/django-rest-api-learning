from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from app.models import Item
from api.items_serializer import ItemSerializer
from rest_framework.renderers import JSONRenderer



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    items = ItemSerializer( Item.objects.all(),many=True)
    # json = JSONRenderer().render(items.data)

    return Response(items.data)
