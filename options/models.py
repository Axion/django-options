# -*- coding: utf-8 -*-
__author__="pykab"
__date__ ="$13.10.2009 8:11:11$"
import datetime
from django.db import models
from django.utils.translation import ugettext as _

class Option(models.Model):
    okey = models.SlugField(
        primary_key=True,
        verbose_name = _('Key')
    )
    ovalue = models.CharField(
        blank=True,
        max_length=255,
        verbose_name = _('Value')
    )
    help = models.TextField(
        blank=True,
        verbose_name = _('Description')
    )
    lastchange = models.DateTimeField(
        verbose_name = _('Last change'),
        default=datetime.datetime.now
    )
    proccessed = models.BooleanField(
        default=False,
        verbose_name = _('Available in templates')
    )

    class Meta:
        verbose_name = _(u'Option')
        verbose_name_plural = _(u'Options')

    def __unicode__(self):
        return u'%s = %s' % (self.okey, self.ovalue)