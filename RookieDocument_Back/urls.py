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
from Base.views import UserListViewSet, TeamViewSet, ContentViewSet, FavViewSet, TeamMemberViewSet, CommentViewSet
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from Base.views import login_submit

router = routers.SimpleRouter()
router.register(r'user', UserListViewSet, 'users')
router.register(r'team', TeamViewSet, 'teams')
router.register(r'content', ContentViewSet, 'contents')
router.register(r'favourite', FavViewSet, 'fav_his')
router.register(r'comment', CommentViewSet, 'fav_his')
router.register(r'teammember', TeamMemberViewSet, 'teammember')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^login/$', login_submit),
    path('docs/', include_docs_urls(title='信息'))
]
