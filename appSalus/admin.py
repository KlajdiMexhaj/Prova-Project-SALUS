from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Salus Admin'

# admin.site.register(Room)

class RoomAdmin(admin.ModelAdmin):

    list_display = ['name','topic']
    list_filter = ['topic']
    list_display_links = ['name','topic']
    search_fields = ['name']
admin.site.register(Room,RoomAdmin)

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Kontakt_Salus)