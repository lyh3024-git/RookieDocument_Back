from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from Base.models import User
from Base.serializer import UserSerializer


class StudentPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class UserListViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    # throttle_classes = (AnonRateThrottle, UserRateThrottle)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StudentPagination
    search_fields = ['name']
    ordering_fields = ['score']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# class Login(APIView):
#     def post(self, request):
#         print(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         status = StudentInfo.objects.filter(username=username, password=password)
#         if status:
#             return Response({'token': 'success'})
#         else:
#             return Response({'token': 'fail'})


def login_submit(request):
    import json
    if request.method == 'POST':
        params = request.body.decode()
        params = json.loads(params)
        username = params.get('username', '')
        password = params.get('password', '')
        status = User.objects.filter(username=username, password=password)

        if status:
            return JsonResponse({'flag': 'success', 'name': username})
        else:
            return JsonResponse({'flag': 'fail'})