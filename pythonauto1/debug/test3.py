# import requests

# # 定义请求的URL和Headers
# url = "http://dev.nexusftx.com:3001/mock/674/uc/ctc/page-query"
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# # 定义查询参数和请求体参数
# params = {
#     "pageNo": 1,
#     "pageSize": 10
# }

# data = {
#     "id": "用户ID",
#     "name": "用户名",
#     "realName": "真实姓名",
#     "location.country": "国家",
#     "location.province": "省份",
#     "location.city": "城市",
#     "location.district": "区县",
#     "location.zipCode": "邮编",
#     "mobilePhone": "手机号",
#     "email": "电子邮件",
#     "memberLevel": "用户等级",
#     "status": "用户状态",
#     "timeZone": "时区",
#     "accountType": "账号类型",
#     "permissions[0]": "账号权限"
# }

# # 发送POST请求
# response = requests.post(url, headers=headers, params=params, data=data)

# # 处理响应
# if response.status_code == 200:
#     # 打印响应内容
#     print("响应内容:")
#     print(response.text)
# else:
#     print("请求失败，状态码:", response.status_code)




import requests

# 定义请求的URL
url = "http://13.215.67.65:8801/uc/login"

# 定义查询参数
params = {
    "username": "15222222222",
    "password": "Wyt123456",
    "captchaVerification": "mockCaptchaVerification"  # 可选，根据接口文档需求填写
}

# 发送GET请求
response = requests.post(url, params=params)
response.encoding='utf-8'

# 处理响应
if response.status_code == 200:
    # 打印响应内容
    print("响应内容:")
    print(response.text)
else:
    print("请求失败，状态码:", response.status_code)




url = "http://13.215.67.65:8801/uc/login"

# 定义查询参数
params = {
    "username": "15222222222",
    "password": "Wyt12345",
    "captchaVerification": "mockCaptchaVerification"  # 可选，根据接口文档需求填写
}

# 发送GET请求
response = requests.post(url, params=params)
response.encoding='utf-8'

# 处理响应
if response.status_code == 200:
    # 打印响应内容
    print("响应内容:")
    print(response.text)
else:
    print("请求失败，状态码:", response.status_code)