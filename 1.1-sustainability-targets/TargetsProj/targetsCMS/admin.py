from django.contrib import admin

from .models import Sequence, Playlist


class SequenceInline(admin.StackedInline):
    model = Sequence
    extra = 0
    list_display = ["PlaylistName"]


class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": (tuple(["PlaylistName", "Active"]),),}),)
    search_fields = ["PlaylistName"]
    inlines = [SequenceInline]
    list_display = ["PlaylistName", "Active"]


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Sequence)
# Register your models here.
