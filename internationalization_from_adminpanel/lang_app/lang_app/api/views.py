from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer
from django.utils import translation

@api_view(['GET'])
def translate_view(request): 
    """  API endpoint that translate product list.  """ 
    try: 
        language = translation.get_language_from_request(request)  
        translation.activate(language) 
        request.LANGUAGE_CODE = translation.get_language() 
        product_list = Product.objects.all() 
        user_serializer = ProductSerializer(product_list, many=True).data 
        return Response({'detail': "Products all listed.", 'messages': user_serializer}, status=status.HTTP_200_OK) 
    except Exception as ex: 
        return Response({"detail": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)