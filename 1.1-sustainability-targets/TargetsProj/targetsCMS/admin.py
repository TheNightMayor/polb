from django.contrib import admin

from .models import Sequence, Playlist


class SequenceInline(admin.TabularInline):
    model = Sequence
    extra = 3
    list_display = ["playlist_text", "pub_date", "was_published_recently"]



class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["playlist_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_filter = ["pub_date"]
    search_fields = ["playlist_text"]
    inlines = [SequenceInline]


admin.site.register(Playlist, PlaylistAdmin)

# Register your models here.
