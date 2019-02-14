# -*- coding: utf-8 -*-
from kernel.api.others import Others

if __name__ == '__main__':

    params = {
        'card_bin': '623145',      # 银行卡卡bin	是	银行卡号前6位
    }

    oth = Others()
    oth.card_bin(params)

