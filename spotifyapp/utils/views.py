from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import ModelSerializer

class ReadWriteViewMixin(GenericViewSet):
    """Mixin view for read and write serializer"""

    read_actions = ['retrieve', 'list']
    read_serializer: ModelSerializer = None
    write_serializer: ModelSerializer = None

    def get_serializer_class(self):
        if self.action in self.read_actions:
            return self.read_serializer
        return self.write_serializer