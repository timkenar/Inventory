from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def query_string(context, **kwargs):
    request = context['request']
    params = request.GET.copy()
    for k, v in kwargs.items():
        params[k] = v
    return urlencode(params)