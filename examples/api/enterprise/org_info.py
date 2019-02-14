# -*- coding: utf-8 -*-
from kernel.api.enterprise import Enterprise

if __name__ == '__main__':

    params = {
        'name': '北京银通易汇科技有限公司',         # 企业名称	否	必须填写企业全称
        # 'enterprise_no': '100',                 # 企业证件号	否	name 或者 enterprise_no 必须有一个不为空
        'country_code': 'CHN',                  # 国家编码	是
    }
    ep = Enterprise()
    ep.org_info(params)

