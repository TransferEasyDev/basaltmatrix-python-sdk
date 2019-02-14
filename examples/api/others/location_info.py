# -*- coding: utf-8 -*-
from kernel.api.others import Others

if __name__ == '__main__':

    params = {
        'location': '22.3169,114.1664',      # 经纬度	是	例如 22.3169,114.1664
    }

    oth = Others()
    oth.lbs_location_info(params)

