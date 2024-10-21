# custom_filters.py
import json
from django import template

register = template.Library()

@register.filter
def json_loads(value):
    return json.loads(value)
