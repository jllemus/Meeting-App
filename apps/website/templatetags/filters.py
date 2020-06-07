from django import template
import json

register = template.Library()

@register.filter(name='add_attr')
def add_attr(value, args):
    string = args.replace("\'", "\"")
    attr_dict = json.loads(string)
    return value.as_widget(attrs=attr_dict)