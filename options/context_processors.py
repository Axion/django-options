# -*- coding: utf-8 -*-
__author__="PyKaB"
__date__ ="$02.07.2009 11:54:40$"
from django.core.cache import cache
from options.models import Option

def options(request):
    options = cache.get('options')
    if options is None:
        items = Option.objects.filter(proccessed=1).values('okey', 'ovalue')
        options = dict([(item['okey'], item['ovalue']) for item in items])
        cache.set('options', options)
   
    return {'options': options}