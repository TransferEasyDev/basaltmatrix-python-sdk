# -*- coding: utf-8 -*-
from kernel.api.individual import Individual

if __name__ == '__main__':

    params = {
        'name': '本',                    # 姓名	是
        # 'doc_no': '',                    # 证件号	否
        # 'doc_type': 'CHN_ID',            # 证件类型	否	当doc_no参数不为空时该参数必填
        # 'country_code': 'CHN_ID',        # country_code	国家编码	否
        # 'dob': '1980/02/05',             # 出生日期	否	格式必须为 yyyy/mm/dd(1980/02/05)形式
        'gender': 'Male',               # 性别	否	Male/Female
        # 'max_match_count': 'CHN_ID',    # 最大匹配数量	否	默认为15，即按分值排序取前15条
        # 'min_score': 'CHN_ID',          # 评分	否	0-100，评分值高于该值的才会返回，默认为90
    }

    ind = Individual()
    ind.screening(params)

