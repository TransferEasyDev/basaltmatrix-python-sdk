# -*- coding: utf-8 -*-
from kernel.api.others import Others

if __name__ == '__main__':

    params = {
        'name': '孔繁明',                                      # 姓名	否	待查询人姓名
        'chn_id_hash': '0a44bae891b9b31a480afa65df14000c',    # 身份证号哈希	是	中国大陆身份证的md5哈希值
    }

    oth = Others()
    oth.screening_chn_id(params)

