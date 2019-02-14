# -*- coding: utf-8 -*-
from kernel.api.enterprise import Enterprise

if __name__ == '__main__':

    params = {
        'name': '北京银通易汇科技有限公司', # 企业名称	是	必须填写企业全称
        'country_code': 'CHN',          # 国家编码	否	请参考附录
        'min_score': '91',              # 最低分值	否	0-100，默认为90
        'max_match_count': '16',        # 返回数量	否	默认为15，即按分值排序取前15条
    }
    ep = Enterprise()
    ep.screening(params)

