from django.contrib import admin
from .models import *


admin.site.register(MainBanner)
admin.site.register(MiniBanner)
admin.site.register(MetaTags)


class PostTariffAdmin(admin.StackedInline):
    model = TariffList


@admin.register(Tariffs)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTariffAdmin]

    class Meta:
        model = Tariffs
