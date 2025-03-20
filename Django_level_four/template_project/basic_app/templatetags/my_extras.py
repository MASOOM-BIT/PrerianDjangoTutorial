
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all occurrences of 'arg' from the string"""
    return value.replace(arg, '')