from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ads.models import Ads
from ads.serializer import AdsSerializers
# Create your views here.


def Kara(request):
    object_list = Ads.objects.all
    return render(request, './index.html', {
        'object_list': object_list,
    })


@api_view(['GET'])
def Karasu(request):
    ads_list = Ads.objects.all()
    serialezer = AdsSerializers(ads_list, many=True)
    return Response(serialezer.data)
