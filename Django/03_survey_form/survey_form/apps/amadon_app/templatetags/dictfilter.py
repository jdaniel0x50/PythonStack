from django.template.defaulttags import register


@register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)


def key(d, key_name):
    try:
        value = d[key_name]
    except KeyError:
        from django.conf import settings
        value = settings.TEMPLATE_STRING_IF_INVALID
    return value

key = register.filter('key', key)
