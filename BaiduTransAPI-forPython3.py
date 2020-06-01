# 百度通用翻译API,不包含词典、tts语音合成等资源
# -*- coding: utf-8 -*-
# flake8: noqa

import http.client, hashlib, urllib, random, json, os


def baidutrans(data):
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  # 原文语种
    toLang = 'en'  # 译文语种
    salt = random.randint(32768, 65536)
    q = data
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def chinese2english(folder_path):
    file_list = os.listdir(folder_path)
    os.chdir(folder_path)
    for old_name in file_list:
        # 中文翻译成英文
        ret = baidutrans(old_name)
        if ret["trans_result"]:
            new_name = ret["trans_result"][0]["dst"]
            os.rename(old_name, new_name)


if __name__ == '__main__':
    path = os.getcwd() + "/document/03_Django framework"
    filelist1 = os.listdir(path)
    for old_path in filelist1:
        folder_path1 = path + "/" + old_path
        chinese2english(folder_path1)
    print("翻译完成")
