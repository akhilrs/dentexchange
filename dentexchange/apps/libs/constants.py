# -*- coding:utf-8 -*-
from .choices import Enumeration
from . import strings

STATE_CHOICES = Enumeration([
    (u'AL', u'AL', u'AL'),
    (u'AK', u'AK', u'AK'),
    (u'AZ', u'AZ', u'AZ'),
    (u'AR', u'AR', u'AR'),
    (u'CA', u'CA', u'CA'),
    (u'CO', u'CO', u'CO'),
    (u'CT', u'CT', u'CT'),
    (u'DE', u'DE', u'DE'),
    (u'FL', u'FL', u'FL'),
    (u'GA', u'GA', u'GA'),
    (u'HI', u'HI', u'HI'),
    (u'ID', u'ID', u'ID'),
    (u'IL', u'IL', u'IL'),
    (u'IN', u'IN', u'IN'),
    (u'IA', u'IA', u'IA'),
    (u'KS', u'KS', u'KS'),
    (u'KY', u'KY', u'KY'),
    (u'LA', u'LA', u'LA'),
    (u'ME', u'ME', u'ME'),
    (u'MD', u'MD', u'MD'),
    (u'MA', u'MA', u'MA'),
    (u'MI', u'MI', u'MI'),
    (u'MN', u'MN', u'MN'),
    (u'MS', u'MS', u'MS'),
    (u'MO', u'MO', u'MO'),
    (u'MT', u'MT', u'MT'),
    (u'NE', u'NE', u'NE'),
    (u'NV', u'NV', u'NV'),
    (u'NH', u'NH', u'NH'),
    (u'NJ', u'NJ', u'NJ'),
    (u'NM', u'NM', u'NM'),
    (u'NY', u'NY', u'NY'),
    (u'NC', u'NC', u'NC'),
    (u'ND', u'ND', u'ND'),
    (u'OH', u'OH', u'OH'),
    (u'OK', u'OK', u'OK'),
    (u'OR', u'OR', u'OR'),
    (u'PA', u'PA', u'PA'),
    (u'RI', u'RI', u'RI'),
    (u'SC', u'SC', u'SC'),
    (u'SD', u'SD', u'SD'),
    (u'TN', u'TN', u'TN'),
    (u'TX', u'TX', u'TX'),
    (u'UT', u'UT', u'UT'),
    (u'VT', u'VT', u'VT'),
    (u'VA', u'VA', u'VA'),
    (u'WA', u'WA', u'WA'),
    (u'WV', u'WV', u'WV'),
    (u'WI', u'WI', u'WI'),
    (u'WY', u'WY', u'WY'),
])

YES_NO_CHOICES = Enumeration([
    (False, 'NO', strings.YES_NO_CHOICES_NO),
    (True, 'YES', strings.YES_NO_CHOICES_YES),
])

PAGINATE_BY = 10
