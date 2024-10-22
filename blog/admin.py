from django.contrib import admin
from blog.models import Post,Category

# Register your models here.

class PostAdmin(admin.modelAdmin):
    list_display = ('title','author','status')
    list_filter = ('status',)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)