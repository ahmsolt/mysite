from django.contrib import admin
from blog.models import Post,Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status')
    list_filter = ('status',)
    search_fields = ['title','contend']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
