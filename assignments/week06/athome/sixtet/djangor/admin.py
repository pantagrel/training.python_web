from django.contrib import admin
from djangor.models import Entry, Archive, Author


#look up ModelAdmin documentation for more options

class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_name', 'entry_text', 'entry_author', 'publish_date', )
    list_filter = ('entry_author', 'publish_date', )
    ordering = ('entry_name', 'entry_author', 'publish_date', )


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('all_entries',)
    ordering = ('all_entries',)     
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('entries_by_author',)
    list_filter = ('entries_by_author',)
    ordering = ('entries_by_author',)



admin.site.register(Entry, EntryAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Author, AuthorAdmin)