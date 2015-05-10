from django.contrib import admin

from models import Artist, ReleaseGroup, Release, Track


@admin.register(Artist, ReleaseGroup, Release, Track)
class GenericAdmin(admin.ModelAdmin):
    pass