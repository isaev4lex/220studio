from django.contrib import admin
from .models import *


admin.site.register(MainBanner)
admin.site.register(MiniBanner)
admin.site.register(WorkSteps)
admin.site.register(ContextAdvertisementTools)
admin.site.register(MetaTags)


class PostImageAdmin(admin.StackedInline):
    model = ContextAdvertisementPossibilities


@admin.register(ContextAdvertisementDescription)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = ContextAdvertisementDescription
