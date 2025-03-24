from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','author','status')
    list_filter = ('status',)
    search_fields = ['title','contend']
    summernote_fields = ('content',)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
