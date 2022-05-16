from django import template

def startswith(value, arg):
    """Removes all values of arg from the given string"""
    return value.startswith(arg)

register = template.Library()


register.filter('startswith', startswith)
