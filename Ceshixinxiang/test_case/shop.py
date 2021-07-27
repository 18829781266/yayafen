# -*- coding: utf-8 -*-
#2021/6/18
import  requests
from configs.fuwudizhi import HOST
from libs.login import Login

class SHOP:
#初始化token
    def __init__(self,token1):
        self.token = {"Authorization":token1}
# 列出店铺接口
    def shop(self,data):
        URL = f"{HOST}/shopping/myShop"
        paylog = data
        res1 = requests.get(url= URL,params=paylog,  headers = self.token)
        return res1.json()
#上传图片接口：
    def file_upload(self,filename,fileDir):
        URL= f'{HOST}/file'
#打开一个文件需要{"变量名",(文件名，文件对象，文件类型)}
        user_file = {"file":(filename,open(fileDir,"rb"),"image/jpeg")}
#去请求上传一个文件格式
        res = requests.post(url = URL,files = user_file,headers = self.token)
        return res.json()["data"]['realFileName']
#更新店铺函数封装需要两个参数，店铺ID，图片信息
    def file_update(self,indata,shopid,imageinfo):
        URL = f'{HOST}/shopping/updatemyshop'
        #1.更新店铺的ID
        indata["id"] = shopid
        #2.更新图片信息
        indata["image"] = f'{HOST}/file/getImgStream?fileName= {imageinfo}'
        indata["image_path"] = imageinfo

        res2 = requests.post(url= URL,data= indata,headers = self.token)
        return res2.json()






if __name__ == '__main__':
 token1 = Login().login({"username":"th0479 ","password":"73a32464b3cb3ac9b59c7eb5b4356730"})["data"]["token"]

 B = SHOP(token1) #B指向那个对象，所以继承这个类的所有属性
# #调用列出商铺列表
# shopid = B.shop({"page":1,"limit":20})["data"]["records"][0]["id"]
# print(shopid)
# #调用上传图片的接口并上传文件
# imageinfo =  B.file_upload("laoguo.jpg","../data/laoguo.jpg")
# #调用更新店铺接口：
# info = {"name": "鱼头在松江店", "address": "上海市普陀区石泉路200号", "description": "好食材自有好味道",
#         "id": 2514, "rating": 4.5, "recent_order_num": 600, "Phone": 18829781266, "category": "快餐便当/简餐",
#         "image_path":12, "image":21}
# response  = B.file_update(info,shopid,imageinfo)
# print(response)





















