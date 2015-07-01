from django.contrib import admin

from models import Profile,Position, Place
# Register your models here.
admin.site.register(Profile)
admin.site.register(Place)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','latitude','longitude','profile')
    list_filter = ('profile__name',)

admin.site.register(Position,PositionAdmin)

