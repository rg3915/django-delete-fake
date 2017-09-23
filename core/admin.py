from django.contrib import admin

from django.db.models import Q
from . import models


@admin.register(models.Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'is_removed']

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model.objects.all(include_removed=True)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
