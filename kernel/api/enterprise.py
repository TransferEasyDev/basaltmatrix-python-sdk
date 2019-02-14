# -*- coding: utf-8 -*-
from kernel.basaltmatrix_request import BasaltmatrixRequest


class Enterprise(object):
    def __init__(self):
        pass

    def org_info(self, params):
        request = BasaltmatrixRequest('enterprise', params)
        request.get()

    def screening(self, params):
        request = BasaltmatrixRequest('screening/org/v2', params)
        request.get()

