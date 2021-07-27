# -*- coding: utf-8 -*-
import xlrd
import json
import os
def get_excel_data(sheet_name,casename):
    #1.获取Excel路径：
    Exceldir = "../data/denglujiekou.xls"
    #2. 把表格加载到内存并保持原样式
    workbook = xlrd.open_workbook(Exceldir,formatting_info=True)
    #3.或者对应的sheet表格
    workSheet = workbook.sheet_by_name(sheet_name)
    #4获取一行
    #print(workSheet.row_values(0))
    #5获取一列
    #print(workSheet.col_values(0))
    #6获取单元格数据（根据坐标）
    #print(workSheet.cell(1,9).values)
    rt = []
    dex = 0 #定义遍历的变量


    for A in workSheet.col_values(0):
        if casename in A:
            reqbodoyData = workSheet.cell(dex,6).value#请求体
            reqData = workSheet.cell(dex,8).value     #响应体
            rt.append((json.loads(reqbodoyData),json.loads(reqData)))#字符串转换字典

            #存储数据列表list
        dex += 1
    return rt

if __name__ == '__main__':
    c = get_excel_data("登陆接口","login")
    print(c)
