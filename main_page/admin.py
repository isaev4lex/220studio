from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(MainBanner)
# admin.site.register(Counter)
admin.site.register(WorkSteps)
admin.site.register(MetaTags)


class PostImageAdmin(admin.StackedInline):
    model = CaseImages


@admin.register(CaseTitle)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = CaseTitle
