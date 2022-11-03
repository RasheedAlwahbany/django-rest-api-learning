from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from app.models import Item


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    items = Item.objects.all()
    items_d=[]
    for item in items:
        items_d=items_d+["name:"+item.name]
    return Response(items_d)