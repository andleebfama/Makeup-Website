from django import template
register = template.Library()
@register.filter(name='reverse_text')
def reverse_text(value):
    return value[::-1]
