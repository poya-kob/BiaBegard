from rest_framework.viewsets import ModelViewSet
from content.api.serializer import ListProductSerializer, DetailProductSerializer
from content.models import Products


class ProductViewset(ModelViewSet):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListProductSerializer
        elif self.action == 'retrieve':
            return DetailProductSerializer
        else:
            return DetailProductSerializer
