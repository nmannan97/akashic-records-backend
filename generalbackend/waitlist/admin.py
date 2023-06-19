# Register your models here.
from django.contrib import admin
from .models import waitlist
class waitlistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['email']}),
        (None,               {'fields': ['phone']}),
        (None,               {'fields': ['position']}),
    ]
    list_display = ('name', 'email', 'phone', 'position')
admin.site.register(waitlist, waitlistAdmin)