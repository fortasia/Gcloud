from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from api.views import TokenView

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/tokens', TokenView)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]