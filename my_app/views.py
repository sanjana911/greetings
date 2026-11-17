from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.


class HelloWorldView(View):

    def get(self,request):

        response_data ={"message":"helloworld"}
        return JsonResponse(response_data)


class GoodmorningView(View):

    def get(self,request):

        response_data = {"message":"good morning"}
        return JsonResponse(response_data)

class GoodafternoonView(View):

    def get(self,request):

        response_data ={"message":"good afternoon"}

        return JsonResponse(response_data)