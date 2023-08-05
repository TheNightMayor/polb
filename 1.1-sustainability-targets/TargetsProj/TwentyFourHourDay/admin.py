from django.contrib import admin

from .models import Sequence, Playlist


class SequenceInline(admin.StackedInline):
    model = Sequence
    extra = 0
    list_display = ["Playlist_Name"]


class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": (tuple(["Playlist_Name", "Active"]),),}),)
    search_fields = ["Playlist_Name"]
    inlines = [SequenceInline]
    list_display = ["Playlist_Name", "Active"]


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Sequence)
# Register your models here.
