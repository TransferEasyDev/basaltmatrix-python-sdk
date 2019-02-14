# -*- coding: utf-8 -*-
from kernel.api.individual import Individual

if __name__ == '__main__':

    params = {
        'doc_type': 'CHN_ID',               # 证件类型	是	中国二代身份证：CHN_ID；护照：PASSPORT
    }

    files = {
        'img': open('/Users/kongfm/Desktop/upload.png') # 证件照片	是	文件流
    }
    ind = Individual()
    ind.ocr(params, files)

