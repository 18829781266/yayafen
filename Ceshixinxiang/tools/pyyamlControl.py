# -*- coding: utf-8 -*-
#2021/7/16
import yaml

def get_yamla_data(filedir):
    fo = open(filedir,"r",encoding= "utf-8")#加载内存
    res = yaml.load(fo,Loader=yaml.FullLoader)#安全模式
    print(res)
    return res

def get_yamlas_data(filedir):
    folist = []#定义一个空列表存储取得数据
    fo = open(filedir,"r",encoding= "utf-8")#加载内存
    res = yaml.load_all(fo,Loader=yaml.FullLoader)#Loader字段是取消安全提醒,读取yaml全部的字段到列表
    for one in res:
        folist.append(one)
    print(folist)
    return folist

# 测试登录接口用例
def get_yamla_case_data(filedir):
    reslist = []
    fo = open(filedir,"r",encoding= "utf-8")#加载内存
    res = yaml.load(fo,Loader=yaml.FullLoader)#安全模式
    del res[0]
    for one in res:
        reslist.append((one["data"],one["resp"]))
    print(reslist)
    return reslist


if __name__ == '__main__':
    get_yamla_case_data("../data/data.yaml")