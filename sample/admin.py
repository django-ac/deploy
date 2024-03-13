from django.contrib import admin

from sample.models import SamplePost


@admin.register(SamplePost)
class SamplePostAdmin(admin.ModelAdmin):
    pass
