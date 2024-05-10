from django.shortcuts import render
from django.conf import settings

# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Jewellery_items
from .serializers import Jewellery_itemsSerializer


class single_jewellery_items_api(GenericAPIView):
    def get(self, request, id):
        queryset = Jewellery_items.objects.get(pk=id)
        serializer = Jewellery_itemsSerializer(queryset)
        return Response(serializer.data)

class all_jewellery_items_api(GenericAPIView):
    serializer_class = Jewellery_itemsSerializer

    def get(self, request):
        user = Jewellery_items.objects.all()
        if (user.count() > 0):
            serializer = Jewellery_itemsSerializer(user, many=True)
            return Response({'data': serializer.data, 'message': 'data get', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'No data available'}, status=status.HTTP_400_BAD_REQUEST)