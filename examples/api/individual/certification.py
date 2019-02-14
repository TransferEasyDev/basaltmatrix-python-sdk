# -*- coding: utf-8 -*-
from kernel.api.individual import Individual

if __name__ == '__main__':

    params = {
        'doc_no': '110301199408190014',         # 证件号码	是
        'name': '孔繁明',                        # 姓名	是
        'doc_type': 'CHN_ID',                   # 证件类型	是	中国二代身份证：CHN_ID
    }
    ind = Individual()
    ind.certification(params)

