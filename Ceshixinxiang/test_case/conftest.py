# -*- coding: utf-8 -*-
#2021/7/8
#有作用域的文件配置，只对当前的包起作用
from libs.login import Login
from configs.fuwudizhi import HOST
from test_case.shop import SHOP
import pytest,os
from libs.login import Login
#fixture  使用技巧
  #1.使用函数名直接调，但是没有返回值
  #@pytest.mark.usefixtures("updata_shop_init")  写入函数名

  #2.需要fixture返回值时，介入一个形参，



#1.能不能在指定的接口前使用fixture？    答：哪里需要，哪里手动执行
#2.fixture 里面的函数不能直接执行
@pytest.fixture(scope='function')
def updata_shop_init():#编写更新店铺的初始化
    print("开始执行")
    #获取登录token
    token1 = Login().login({"username": "th0479 ", "password": "73a32464b3cb3ac9b59c7eb5b4356730"})["data"]["token"]
    B = SHOP(token1)
    # 调用列出商铺列表
    shopid = B.shop({"page": 1, "limit": 20})["data"]["records"][0]["id"]
    print(shopid)
    # 调用上传图片的接口并上传文件
    imageinfo = B.file_upload("laoguo.jpg", "../data/laoguo.jpg")
    return shopid,imageinfo
@pytest.fixture(scope='function')
def start_running():
    print("开始执行")
# 清楚报告数据
    try:
        for one in os.listdir("../report/tmp"):
            if 'json' in one or "txt" in one:
                os.remove(f"../report/tmp{one}")
    except:
        print("第一次执行框架数据")


    yield
    print("执行结束")

