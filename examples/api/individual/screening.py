# -*- coding: utf-8 -*-
from kernel.api.individual import Individual

if __name__ == '__main__':

    params = {
        'name': '本',                    # 姓名	是
        # 'country_code': 'CHN_ID',        # country_code	国家编码	否
        # 'dob': '1980/02/05',             # 出生日期	否	格式必须为 yyyy/mm/dd(1980/02/05)形式
        'gender': 'Male',               # 性别	否	Male/Female
        # 'max_count': '15',              # 最大匹配数量	否	默认为20，即按分值排序取前20条
        # 'min_score': 'CHN_ID',        # 评分	否	0-100，评分值高于该值的才会返回，默认为90
    }

    ind = Individual()
    ind.screening(params)

