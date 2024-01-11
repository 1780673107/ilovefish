# import os
# import random
# import unittest
# from pack_lib.ddt import ddt, data
# from common.read_excel import ReadExcel
# from common.http_requests import HTTPRequest
# from common.mylogger import log
# from common.constant import DATA_DIR
# # from common.do_mysql import ReadSQL
# from common.conifg import myconf
# from common.text_replace import data_replace
# from common.regis import send_sms_verification_code,random_phone,register_user
import requests
import json
from regis import send_sms_verification_code,random_phone,register_user


    
def login(phone):

    # 登录
    url = "http://13.215.67.65:8801/uc/login"  
    data = {
    "username": phone, 
    "password": 'Wyt123456',
    "captchaVerification":"mockCaptchaVerification"}
    
    response=requests.post(url, data)
    response.encoding = 'utf-8'
        # 解析响应文本为JSON  
    response_json = response.json()  
    print(response_json)
    # 检查登录是否成功，并提取token（如果存在）  
    if response_json.get('code') == 0 and response_json.get('message') == 'SUCCESS':  
        data = response_json.get('data')  
        if data:  
            token = data.get('token')  
            if token:  
                return token  
            else:  
                print("登录成功，但未返回token")  
        else:  
            print("登录成功，但未返回数据")  
    else:  
        print("登录失败:", response_json.get('message'))  
          
    return None
    

phone=random_phone()
username,phone=register_user()
login_response = login(phone)  
token=login_response
print(token)


