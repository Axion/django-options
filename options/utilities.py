# -*- coding: utf-8 -*-

from django.core.cache import cache
from options.models import Option

def option_by_key(key):
    try:
        return Option.objects.get(okey=key).ovalue
    except:
        return 0
