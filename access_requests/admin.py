from django.contrib import admin
from .models import AccessRequest

from .models import AccessRequest, AuditLog

admin.site.register(AccessRequest)
admin.site.register(AuditLog)
