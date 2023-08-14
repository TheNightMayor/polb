from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Story, Content, Topic



class TopicInline(admin.StackedInline):
    model = Topic
    extra = 0
    filter_horizontal = ['stories']

class ContentAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": (tuple(["Title", "Attract"])),}),)
    search_fields = ["Title"]
    list_display = ["Title", "Attract"]
    inlines = [TopicInline]
    pass

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['Title', 'stories']})]
    search_fields = ['Title']
    list_display = ['Title']
    pass
    
class StoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['Headline', 'Overview', 'Media']})]
    search_fields = ['Headline']
    list_display = ['Headline', 'Overview', 'Media']
    pass
    
        
        
admin.site.register(Story, StoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Topic, TopicAdmin)
# Register your models here.
