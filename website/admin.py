from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Contact,ContactAdmin)