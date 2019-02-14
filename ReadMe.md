
![BasaltMatrix](https://s.transfereasy.com/logo/bm_banner.png)

# 汇通天下, 无处不达

* [官方网站](https://www.basaltmatrix.com)
* [体验中心](https://cdd.basaltmatrix.com/record/enterprise)
* [开发文档](https://www.basaltmatrix.com/Home/tutorial)


## 结构

```$xslt
├── config      # 配置文件
├── examples    # DEMO
├── kernel      # API
└── test        # 测试用例

```

## 示例

```
/**
 * 初始化环境
 */

$ cd basaltmatrix-python-sdk
$ virtualenv ENV
$ source ./ENV/bin/active
$ (ENV) pip install -r requirements.txt

```

```
/**
 * 配置文件
 * 
 * └── config
 *     └── __init__.py
 */

# 在 __init__.py 中控制生产和测试的配置文件开关
from config.prod import *  # 生产环境
```

```
/**
 * 配置文件
 *
 * └── config
 *     └── prod.py
 */
BM_HOST = 'https://testapi.basaltmatrix.com/{url}'
AGENT_NO = 'your_agent_no'
AGENT_KEY = 'your_agent_key'
```

```python
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

```

## 依赖

* Schemer==0.2.11
* requests==2.18.4
* Flask==1.0.2
* nose==1.3.7