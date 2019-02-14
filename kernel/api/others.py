# -*- coding: utf-8 -*-
from kernel.basaltmatrix_request import BasaltmatrixRequest


class Others(object):
    def __init__(self):
        pass

    def card_bin(self, params):
        request = BasaltmatrixRequest('card_bin', params)
        request.get()

    def lbs_ip_info(self, params):
        request = BasaltmatrixRequest('lbs/ip_info', params)
        request.get()

    def lbs_location_info(self, params):
        request = BasaltmatrixRequest('lbs/location_info', params)
        request.get()

    def screening_chn_id(self, params):
        request = BasaltmatrixRequest('screening/chn_id', params)
        request.get()


