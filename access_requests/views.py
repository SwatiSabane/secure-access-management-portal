from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import AccessRequest
from .serializers import AccessRequestSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AccessRequest, AuditLog


class AccessRequestViewSet(viewsets.ModelViewSet):

    serializer_class = AccessRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.role in ['admin', 'manager']:
            return AccessRequest.objects.all()

        return AccessRequest.objects.filter(
            requested_by=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            requested_by=self.request.user
        )

    @action(
    detail=True,
    methods=['post'])

    def approve(self, request, pk=None):

        if request.user.role not in ['manager', 'admin']:
            return Response(
            {"error": "Permission denied"},
            status=403
        )

        access_request = self.get_object()

        access_request.status = 'APPROVED'
        access_request.save()

        AuditLog.objects.create(
        access_request=access_request,
        action='APPROVED',
        performed_by=request.user
    )

        return Response(
        {"message": "Request approved"}
    )

    @action(
    detail=True,
    methods=['post'])

    def reject(self, request, pk=None):

        if request.user.role not in ['manager', 'admin']:
            return Response(
            {"error": "Permission denied"},
            status=403
        )

        access_request = self.get_object()

        access_request.status = 'REJECTED'
        access_request.save()

        AuditLog.objects.create(
        access_request=access_request,
        action='REJECTED',
        performed_by=request.user
    )

        return Response(
        {"message": "Request rejected"}
    )