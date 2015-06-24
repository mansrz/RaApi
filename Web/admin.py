from django.contrib import admin

from models import Profile,Position
# Register your models here.
admin.site.register(Profile)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','latitude','longitude','profile')
    list_filter = ('profile__name',)

admin.site.register(Position,PositionAdmin)

