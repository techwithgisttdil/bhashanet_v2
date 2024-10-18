import django_filters
from .models import *

class IDNWebsiteFilter(django_filters.FilterSet):
    class Meta:
        model = IDNReadyWebsitesLangugeURLMapping
        fields = ['IDNReadyWebsites']