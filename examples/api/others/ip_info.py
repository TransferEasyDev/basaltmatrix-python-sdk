# -*- coding: utf-8 -*-
from kernel.api.others import Others

if __name__ == '__main__':

    params = {
        'ip': '45.120.217.225',      # IP地址	是
    }

    oth = Others()
    oth.lbs_ip_info(params)

