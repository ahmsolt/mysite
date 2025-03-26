from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','author','status')
    list_filter = ('status',)
    search_fields = ['title','contend']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
     date_hierarchy = 'created_date'
     empty_value_display = '-empty-'
     list_display = ('name','post','approved','created_date')
     list_filter = ('post','approved')
     search_fields = ['name','contend']
     

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
