#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2014 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.db import models
import django_filters
from django_filters.filters import RangeFilter, DateTimeFilter, DateRangeFilter
from cdr.models import CDR


#
# this is a work in progress on integrating https://django-filter.readthedocs.org/
#

# Add in views.py
# f = CDRFilter(request.GET, queryset=CDR.objects.filter(destination_number__startswith='+346'))
# pass the following to the template:
# 'filter': f,

# Then in template display with

#     <form action="" method="get">
#         {{ filter.form.as_p }}
#         <input type="submit" />
#     </form>
#     {% for obj in filter %}
#         {{ obj.name }} - ${{ obj.price }}<br />
#     {% endfor %}


class CDRFilter(django_filters.FilterSet):
    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }
    duration = RangeFilter()
    billsec = RangeFilter()
    starting_date = DateRangeFilter()

    class Meta:
        model = CDR
        fields = ['switch', 'caller_id_number', 'starting_date', 'duration', 'billsec']