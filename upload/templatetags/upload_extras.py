from django import template

register = template.Library()

@register.filter('filename')
def filename(value):
    folder, filename=value.split("/")
    return filename