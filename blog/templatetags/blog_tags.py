from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='plustwo')
def function(a=5):
    return a + 2

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts