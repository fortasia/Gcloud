from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin


from api.serializers import TokenSerializer
from api.models import Token


class TokenView(viewsets.ModelViewSet):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super(TokenView, self).list(request, *args, **kwargs)