# -*- coding: utf-8 -*-
import pytest,os
from tools.Excel import get_excel_data
from libs.login import Login
from tools.pyyamlControl import get_yamla_case_data
#封装测试类
# #get_excel_data("登陆接口","login")
# for one in get_excel_data("登陆接口","login"):
#       bodydata = one[0]#请求体
#       respdata = one[1]#响应体
# r = Login().login("bodydata")
#  封装测试类

class Test_login:
    @pytest.mark.parametrize("inBody,exspData",get_yamla_case_data("../data/data.yaml"))  # 数据驱动固定语法，首先两个变量名然后赋
    def test_login(self,inBody,exspData):
        res = Login().login(inBody)
        #调用登录接口代码
        #做断言：
        print("--正在执行--")
        assert res["msg"] == exspData["msg"]
if __name__ == '__main__':
  pytest.main(["test_login.py","-s","--alluredir","../report/tmp"])
  # 设置报告防止的路径1.用pytest生成报告需要的文件 2.使用allure生成可视化报告
  os.system("allure serve ../report/tmp")
  #  启动 allure 服务，不能关闭pycharm，设置默认浏览器谷歌和火狐


