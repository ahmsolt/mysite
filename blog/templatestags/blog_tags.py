from django import template

register = template.Library()


@register.simple_tag(name='plustwo')
def hello():
    return 'hello'