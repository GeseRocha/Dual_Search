import math
from django import template
from .. import *


register = template.Library()


@register.inclusion_tag('main/pagination.html', takes_context=True)
def show_pagination(context, pages_to_show=10):

    """ Find the last possible page """
    last_page = math.ceil(context['total_results'] / 10)

    """ The last page will be either the
        user-specified maximum page, or the
        last page that was returned, whichever
        was lower """
    last_page = min([10, int(last_page)])

    prev_page = context['current_page'] - 1

    next_page = context['current_page'] + 1

    context.update({
        'pages': range(1, last_page + 1),
        'prev_page': prev_page if context['current_page'] - 1 > 0 else None,
        'next_page': next_page if next_page < last_page else None,
    })

    return context