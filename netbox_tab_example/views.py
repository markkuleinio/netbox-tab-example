from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from ipam.models import Prefix
from utilities.views import ViewTab, register_model_view


@register_model_view(Prefix, name="tab-example")
class TabExampleView(PermissionRequiredMixin, View):
    permission_required = "ipam.view_prefix"
    tab = ViewTab(
        label="Tab Example",
        permission="ipam.view_prefix",
    )

    def get(self, request, pk):
        prefix = Prefix.objects.get(pk=pk)
        return render(
            request,
            "netbox_tab_example/tab_example.html",
            context={
                "object": prefix,
                "tab": self.tab,
            },
        )

