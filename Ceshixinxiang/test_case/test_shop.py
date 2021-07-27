# -*- coding: utf-8 -*-
#2021/7/8

import pytest
import json
from test_case.shop import SHOP
from libs.login import Login
from tools.Excel import get_excel_data
from test_case.conftest import updata_shop_init
@pytest.mark.usefixtures('updata_shop_init')
# # class Testshop:
# def setup_class(self):#这个测试类的每一个接口都需要登录的token
#     self.token = Login.login({"username":"th0479 ","password":"73a32464b3cb3ac9b59c7eb5b4356730"})["data"]["token"]
#     self.shopObject = SHOP(self.token) #创建店铺实例
# #列出店铺
# def test_shop_list(self):
#     res = self.shopObject.shop({"page": 1, "limit": 20})
# # #做断言, 需要多个断言时,用OR或者and ，就是一个布尔表达式
# #更新店铺
def test_shop_updata(self,inBody,expData,updata_shop_init):
    res = self.shopObject.test_shop_updata(inBody,updata_shop_init[0],updata_shop_init[1])
    #做断言, 需要多个断言时,用OR或者and ，就是一个布尔表达式
    return res
if __name__ == '__main__':
    pytest.main(["test_shop.py","-s"])





#更新店铺