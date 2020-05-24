from rest_framework import viewsets
from rest_framework.response import Response
from guardian.shortcuts import assign_perm

from permissions.services import APIPermissionClassFactory
from users.models import Reader
from users.serializers import ReaderSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ReaderPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': True,
                    'partial_update': True,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        reader = serializer.save()
        user = self.request.user
        assign_perm('reader.view_reader', user, reader)
        assign_perm('reader.change_reader', user, reader)
        return Response(serializer.data)
