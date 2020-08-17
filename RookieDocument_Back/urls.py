"""RookieDocument_Back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from Base.views import UserListViewSet, ContentViewSet, TeamViewSet, FavViewSet
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from Base.views import login_submit


router = routers.SimpleRouter()
router.register(r'users', UserListViewSet, 'users')
router.register(r'teams', TeamViewSet, 'teams')
router.register(r'contents', ContentViewSet, 'contents')
router.register(r'fav_his', FavViewSet, 'fav_his')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^login/$', login_submit),
    path('docs/', include_docs_urls(title='信息')),
    # url(r'^upload_img/$', doc_view.upload_img),
    # url(r'^media/(?P<name>\d+).(?P<postfix>\w+)', doc_view.get_media),
]
