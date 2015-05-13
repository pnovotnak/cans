from django.contrib import admin

from models import Artist, ReleaseGroup, Release, Track
from models import Queue


@admin.register(Artist, ReleaseGroup, Release, Track, Queue)
class GenericAdmin(admin.ModelAdmin):
    pass