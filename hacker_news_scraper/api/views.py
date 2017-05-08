# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from functools import partial

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_tree(request, format=None):
    """
    API Tree
    """
    r = partial(reverse, request=request, format=format)
    return Response(OrderedDict([
        ('post', OrderedDict([
            ('list', r('api:post-list')),
            ('detail', r('api:post-detail', args=[1]))
        ]))
    ]))


api_tree.permission_classes = ()
