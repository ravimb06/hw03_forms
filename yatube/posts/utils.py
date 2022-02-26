from django.core.paginator import Paginator


def obj_in_page(request):
    return 10


def posts_paginator(obj, count, page_number):
    paginator = Paginator(obj, count)
    page_obj = paginator.get_page(page_number)
    return page_obj
