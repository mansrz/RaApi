from django.contrib import admin

from models import PlaceType,Position
# Register your models here.
admin.site.register(PlaceType)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','latitude','longitude','place')
    list_filter = ('place__name',)

admin.site.register(Position,PositionAdmin)

