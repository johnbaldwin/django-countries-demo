from django.contrib import admin

from .models import (
    CountryInfo,
    LinkSet,
    CountryPageLink,
    )

admin.site.register(CountryInfo)
admin.site.register(LinkSet)
admin.site.register(CountryPageLink)
