# coding=utf8

import requests
import hashlib
import random
import sys

# appid & key from baidu fanyi
appid ='xxxxxxxx'
secretKey ='xxxxxxxxxxx'

def baidu_fanyi(query):
    salt = random.randint(1, 10)
    code = appid + query + str(salt) + secretKey
    sign = hashlib.md5(code.encode()).hexdigest()
    api = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    data = {
        "q": query,
        "from": "auto",
        "to": "auto",
        "appid": appid,
        "salt": salt,
        "sign": sign
    }

    response = requests.post(api, data)
    try:
        result = response.json()
        dst = result.get("trans_result")[0].get("dst")

    except Exception as e:
        dst = query

    finally:
        return dst

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage, %s string"%(sys.argv[0]))
        exit(-1)
    ret = baidu_fanyi(sys.argv[1])
    print(ret)

