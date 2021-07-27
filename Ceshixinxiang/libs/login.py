#-*- coding: utf-8 -*-

#封装的登录类
import requests
from configs.fuwudizhi import HOST

class Login:
    def login(self,indata):
        URL =f'{HOST}/account/sLogin'
        paylod = indata
        res = requests.post(url = URL,data= paylod)
        #return res.json()['data']['token']
        return res.json()
if __name__ == '__main__':
    res = (Login().login({"username":"th0479 ","password":"73a32464b3cb3ac9b59c7eb5b4356730"}))["data"]["token"]
    print(res)

