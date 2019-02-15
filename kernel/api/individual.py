# -*- coding: utf-8 -*-
from kernel.basaltmatrix_request import BasaltmatrixRequest


class Individual(object):
    def __init__(self):
        pass

    def certification(self, params):
        request = BasaltmatrixRequest('individual/doc/certification', params)
        request.get()

    def ocr(self, params, files):
        request = BasaltmatrixRequest('individual/doc/ocr', params, files)
        request.post()

    def screening(self, params):
        request = BasaltmatrixRequest('screening/individual/v2', params)
        request.get()


