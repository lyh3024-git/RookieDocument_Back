from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from Base.models import User, Team, Content, Fav_His, TeamMember, Comment, Favourite
from Base.serializer import UserSerializer, TeamSerializer, ContentSerializer, Fav_HisSerializer, TeamMemberSerializer, \
    CommentSerializer


class Genericpgination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class UserListViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, UpdateModelMixin):
    # throttle_classes = (AnonRateThrottle, UserRateThrottle)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Genericpgination
    search_fields = ['username']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'code': 0, 'msg': 'success'}, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        # 查询用户的详情信息 前端通过 /users/1/ 查询
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # 修改密码信息 必须转id username password
        # 修改成功后 后台返回类似 作为修改成功的判断 {"flag": "success", "name": "admin", "id": 1}
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return JsonResponse({'flag': 'success', 'name': instance.username, 'id': instance.id})

    def perform_update(self, serializer):
        print(serializer)
        serializer.save()


class Login(APIView):
    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        status = User.objects.filter(username=username, password=password)
        if status:
            return Response({'token': 'success'})
        else:
            return Response({'token': 'fail'})


def login_submit(request):
    import json
    if request.method == 'POST':
        params = request.body.decode()
        params = json.loads(params)
        username = params.get('username', '')
        password = params.get('password', '')
        status = User.objects.filter(username=username, password=password)

        if status:
            # 登录成功会 返回用户的id  作为查询用户和修改密码的依据
            return JsonResponse({'flag': 'success', 'name': username, 'id': status.first().id})
        else:
            return JsonResponse({'flag': 'fail'})


class TeamViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = Genericpgination
    search_fields = ['name']


class ContentViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    # 内容创建  创建成功返回  {'flag': 'success'}
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = Genericpgination
    search_fields = ['content']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'flag': 'success'}, status=status.HTTP_201_CREATED, headers=headers)


class TeamMemberViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    pagination_class = Genericpgination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'flag': 'success'}, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = Genericpgination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'flag': 'success'}, status=status.HTTP_201_CREATED, headers=headers)


class FavViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Favourite.objects.all()
    serializer_class = Fav_HisSerializer
    pagination_class = Genericpgination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'flag': 'success'}, status=status.HTTP_201_CREATED, headers=headers)


class ContentViewSet(ListAPIView, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    # 内容创建  创建成功返回  {'flag': 'success'}
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # pagination_class = Genericpgination
    search_fields = ['content']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'flag': 'success'}, status=status.HTTP_201_CREATED, headers=headers)