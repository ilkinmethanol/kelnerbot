from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerOrderSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class helloApi(APIView):
    """test api"""

    serializer_class =  CustomerOrderSerializer
    @csrf_exempt
    def get(self,request,format=None):

        an_apiview = [
            1,2,3,4,65,6,7,9,33
        ]

        return Response({"message":"hello","anapi":an_apiview})
    @csrf_exempt
    def post(self,request):
        serializer = CustomerOrderSerializer(data=request.data)

        if serializer.is_valid():
            table_num = serializer.data.get('table_num')
            ordered_at = serializer.data.get('ordered_at')
            final_amount = serializer.data.get('final_amount')
            orders = serializer.data.get('orders')

            message = 'hello {0}'.format(table_num)
            print("-------------------------")
            print(table_num)
            print(ordered_at)
            print(final_amount)
            print(orders)
            print("------------------------")
            return Response({"message":message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)