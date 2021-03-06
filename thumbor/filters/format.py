#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.filters import BaseFilter, filter_method


ALLOWED_FORMATS = ['png', 'jpeg', 'webp']


class Filter(BaseFilter):

    @filter_method(BaseFilter.String)
    def format(self, format):
        if format.lower() not in ALLOWED_FORMATS:
            self.context.request.format = None
        else:
            self.context.request.format = format.lower()
