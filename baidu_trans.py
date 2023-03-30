# coding=utf8

import requests
import hashlib
import random
import sys
import time
import os
import configparser

appid = ""
secretkey = ""

def load_config(file):
    config = configparser.ConfigParser()
    config.read(file, encoding='utf-8')
    return config.get('baidu', 'appid'), config.get('baidu', 'secretkey')

def baidu_fanyi(query):
    salt = random.randint(1, 10)
    code = appid + query + str(salt) + secretkey
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

    conf_file = "./apikey.conf"
    if os.path.exists(conf_file):
        appid, secretkey = load_config(conf_file) 

    lines = sys.argv[1].split('\n', 10)
    for line in lines:
        ret = baidu_fanyi(line)
        print(ret)
        time.sleep(1)

