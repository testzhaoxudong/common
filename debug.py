# list1 = ['西西','边边','a1', '马', 'TY','清心']
# #  列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
# # 方法1： 手动扩充--字典--存放在列表里面；{}
# # 方法2： 自动--dict（）--不强制 list.appen()
# # list2 =
# dict1 = {"西西":['西西','男','18','济南'],"边边":['边边','男','18','山东']}
# list2 = [dict1]
# print(list2)
# list2["key"] = input("name：")
# for dict1["key"] in list1:
#     if dict1["key"] == "西西":
#         print(dict1["西西"])
#     elif dict1["key"] == "边边":
#         print(dict1["边边"])

# 案例2：获取dictory里的信息，并且把url的value值， data中嵌套字典的每个value值，按行输出
import json

# dictory={'url':'http://www.baidu.com','data':{'username':'admin','pwd':'123456'}}
# for i in dictory:
#     print(dictory[i])
#     if i == 'data':
#         for j in dictory[i].values():
#             print(type(dictory[i]))
#             print(dictory[i])
# print(type(dictory))
# a = dictory["url"]
# print(dictory["url"])
# print(type(a))




# print(dictory['url'].values())
# a = dict(dictory['url'])
# print(type(dictory["url"]))
# print(dictory.items())
import requests

import time

# TIME = time.strftime("%Y%m%d%H%M%S")
# print(TIME)
# name = input("请输入姓名：")
# class_b = input("请输入班级:")
# lst1 = [...]
# lst1.append(name)
# lst1.append(lst1)
# print(lst1)


# list_1 = [1, 'python', 'selenium', 'postman', True, 123.345, 'python']
# 1. 将列表反转
# list_1.reverse()
# print(list_1)
# 2. 获取'selenium'的索引值
# l1 = list_1.index("selenium")
# print(l1)
# 3. 统计python的个数
# print(list_1.count("python"))
# 4. 删除lst中所有的python元素
# sum = list_1.count("python")
# del list_1[list_1.index(["python"]*sum)]
# print(list_1)

# url = "http://119.3.13.80:81/mer-queue/health/getHealthCodeInfo"
# data = {
#     "cardNumber":"371324199311205218",
#     "userName":"马志燃"
# }
# headers = {
#     "Blade-Auth":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ0ZW5hbnRfbmFtZSI6bnVsbCwidXNlcl9uYW1lIjoiaGVhbHRoX2NvZGVfYWNjZXNzX3Rva2VuX2FkbWluIiwidXNlcl9mcmVlemVfZmxhZyI6IjAiLCJhdmF0YXIiOiIiLCJhdXRob3JpdGllcyI6WyJhZG1pbiJdLCJjbGllbnRfaWQiOiJrc3B0IiwiZGF0YV9zb3VyY2UiOm51bGwsInJvbGVfbmFtZSI6ImFkbWluIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwidXNlcl90eXBlIjpudWxsLCJjb21wYW55bm8iOm51bGwsInVzZXJfaWQiOiIxNDcxNDIyNzY0NzIwMjIwNzI4Iiwicm9sZV9pZCI6IjIwMjAxMTEzMTc1MzAxIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IuiOt-WPlumJtOadg-eUqOaIt--8jOS4jeWPr-WIoOmZpCIsImNsaWVudCI6bnVsbCwiZXhwIjoxNjU5MzU3MDc3LCJkZXB0X2lkIjoiMTE2OTUyNjMyMDI0NjM4NjY5MCIsImp0aSI6ImZkNWQ0OGNiLTBlOGMtNGFjNi1iMDE4LWU3ZGUzMjQyMTZiOCIsImFjY291bnQiOiJoZWFsdGhfY29kZV9hY2Nlc3NfdG9rZW5fYWRtaW4ifQ.uff6pUChzwna7LYxXUXZNxJHBj3nmy6KVZAejnRkOic",
#     "Authorization":"Basic a3NwdF9kcml2ZXI6c2Fhc19rc3B0X2RyaXZlcg==",
#     "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ0ZW5hbnRfbmFtZSI6bnVsbCwidXNlcl9uYW1lIjoiaGVhbHRoX2NvZGVfYWNjZXNzX3Rva2VuX2FkbWluIiwidXNlcl9mcmVlemVfZmxhZyI6IjAiLCJhdmF0YXIiOiIiLCJhdXRob3JpdGllcyI6WyJhZG1pbiJdLCJjbGllbnRfaWQiOiJrc3B0IiwiZGF0YV9zb3VyY2UiOm51bGwsInJvbGVfbmFtZSI6ImFkbWluIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwidXNlcl90eXBlIjpudWxsLCJjb21wYW55bm8iOm51bGwsInVzZXJfaWQiOiIxNDcxNDIyNzY0NzIwMjIwNzI4Iiwicm9sZV9pZCI6IjIwMjAxMTEzMTc1MzAxIiwic2NvcGUiOlsiYWxsIl0sIm5pY2tfbmFtZSI6IuiOt-WPlumJtOadg-eUqOaIt--8jOS4jeWPr-WIoOmZpCIsImNsaWVudCI6bnVsbCwiZXhwIjoxNjU5MzU3MzI3LCJkZXB0X2lkIjoiMTE2OTUyNjMyMDI0NjM4NjY5MCIsImp0aSI6IjgzM2ZlYTUzLTMwNTMtNDY1Ny04MGJiLWEwMTk2NWQ4NmVlNyIsImFjY291bnQiOiJoZWFsdGhfY29kZV9hY2Nlc3NfdG9rZW5fYWRtaW4ifQ.f66yyqb0x6Npy4S6K_8Y8olYcAtZYCwcP75PJHFkF1A"
# }
#
# res = requests.post(url=url,params=data,headers=headers)
#
# print(res.json())


url = "http://36.133.124.14:89/api/shipper-auth/oauth/token"
data = {
    'password':'123456',
    'tenantId':'847975',
    'type':'account',
    'username':'山东仁华建材有限公司',
    'grant_type':'password',
    'scope':'all',
}
headers = {
    'Accept':'application/json',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Authorization':'Basic a3NwdF9zaGY6c2Fhc19rc3B0X3NoZg==',
    'Content-Length':'669',
    'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryMb3zMfHZuksvH1uD',
    'Host':'36.133.124.14:89',
    'Origin':'http://36.133.124.14:89',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://36.133.124.14:89/',
    'Tenant-Id':'847975',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
}
res = requests.post(url,data,headers=headers)
print(res.status_code,res.cookies)
















