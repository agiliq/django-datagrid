import urllib
from django import template
register = template.Library()


PAGINATION_DEFAULT = 20
@register.inclusion_tag('datagrid/pagination_size_frag.html', takes_context=True)
def render_pagination_size_widget(context):
    "Usage {% render_pagination_size_widget %}"
    payload = {}
    payload['page_sizes'] = [1, 10, 20, 50, 100, 500]
    if 'request' in context:

        request = context['request']
        getvars = request.GET.copy()
        if 'page_size' in getvars:
            payload['current_page_size'] = int(getvars['page_size'])
            del getvars['page_size']
        else:
            from django.conf import settings
            payload['current_page_size'] = getattr(settings, 'PAGINATION_DEFAULT_PAGINATION', PAGINATION_DEFAULT)
        if 'page' in getvars:
            del getvars['page']
        if len(getvars.keys()) > 0:
            payload['getpagingvars'] =  zip(getvars.keys(), getvars.values())
        else:
            payload['getpagingvars'] = []
    return payload


@register.inclusion_tag('datagrid/get_pdf_link.html', takes_context=True)
def get_pdf_link(context):
    getvars = {}
    if 'request' in context:
        request = context['request']
        getvars = request.GET.copy()
        getvars['is_pdf'] = 1
        getvars = urllib.urlencode(getvars)
        return {'getvars':getvars}
    else:
        getvars['is_pdf'] = 1
        getvars = urllib.urlencode(getvars)
    return {'getvars':getvars}


@register.inclusion_tag('datagrid/get_csv_link.html', takes_context=True)
def get_csv_link(context):
    getvars = {}
    if 'request' in context:
        request = context['request']
        getvars = request.GET.copy()
        getvars['is_csv'] = 1
        getvars = urllib.urlencode(getvars)
    else:
        getvars['is_csv'] = 1
        getvars = urllib.urlencode(getvars)
    return {'getvars':getvars}

@register.inclusion_tag('datagrid/get_search_form.html', takes_context=True)
def get_search_form(context):
    getvars = {}
    if 'request' in context:
        request = context['request']
        getvars = request.GET.copy()
        if 'q' in getvars:
            searchterm = getvars['q']
            del getvars['q']
            return {'getvars':getvars.items(), 'searchterm': searchterm}
        else:
            return {'getvars':[], 'searchterm': ''}

@register.inclusion_tag('datagrid/get_filter_form.html', takes_context=True)
def get_filter_form(context):
    #TODO

    return context



@register.inclusion_tag('datagrid/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=3):
    """
    Renders a paginator used for jumping between pages of results.
    """
    page_nums = range(max(1, context['page'] - adjacent_pages),
                      min(context['pages'], context['page'] + adjacent_pages)
                      + 1)
    getvars = {}
    if 'request' in context:
        request = context['request']
        getvars = request.GET.copy()
        if 'page' in getvars:
            getvars['page']
    getvars = urllib.urlencode(getvars)

    return {
        'hits': context['hits'],
        'results_per_page': context['results_per_page'],
        'page': context['page'],
        'pages': context['pages'],
        'page_numbers': page_nums,
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_nums,
        'show_last': context['pages'] not in page_nums,
        'extra_query': context.get('extra_query', None),
        'getvars': getvars,
    }
