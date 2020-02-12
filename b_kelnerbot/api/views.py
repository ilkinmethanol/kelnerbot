from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class helloApi(APIView):
    """test api"""

    def get(self,request,format=None):

        an_apiview = [
            1,2,3,4,65,6,7,9,33
        ]

        return Response({"message":"hello","anapi":an_apiview})