
import requests  
import random  
import json
import string  

import requests
import json
from common.regis import random_phone,register_user



# class phon_test():
#     # def __init__(self):  
#     #     self.username = None
#     #     self.phone = None
#     #     self.password = 'Wyt123456'
#     def random_phone():  
#         second = random.choice([3, 4, 5, 7, 8])  
#         third = {  
#             3: random.randint(0, 9),  
#             4: random.choice([5, 7, 9]),  
#             5: random.choice([i for i in range(10) if i != 4]),  
#             7: random.choice([i for i in range(10) if i not in [4, 9]]),  
#             8: random.randint(0, 9),  
#         }[second]  
#         suffix = random.randint(9999999, 100000000)  
#         phone = "1{}{}{}".format(second, third, suffix)  
#         return phone

#     def generate_random_username(self):  
#         # 随机选择3个字母  
#         random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))  
#         # 随机选择3个数字  
#         random_digits = ''.join(random.choices(string.digits, k=3))  
#         # 组合用户名  
#         username = "Wyt123" + random_letters + random_digits  
#         return username


#     def send_sms_code(): 
#         url = 'http://13.215.67.65:8801/uc/mobile/code'  
#         data = {"phone": phone, "country": "阿富汗"}  
#         response = requests.post(url, data=data)  
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#         return response.text  

#     def register():  
#         url = 'http://13.215.67.65:8801/uc/register/phone'  
#         data = {  
#             'phone': phone,
#             'username': username,  
#             'password': "Wyt123456",  
#             'captchaVerification': 'captchaVerification',  
#             "country": "阿富汗",    
#             "code": "999999",
#             "promotion": ""

#         }  
#         response = requests.post(url, data=data)  
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode 
#         print(phone,username) 
#         return response.text  
    



#     def login(self):  
#         url = 'http://dev.nexusftx.com:8801/uc/login'  
#           # 设置请求头为JSON内容类型  
#         data = {  
#             "username": self.generate_random_username(),   
#             "password": "Wyt123456",  
#             "captchaVerification": "mockCaptchaVerification"  
#         }  
#         response = requests.post(url, data=data)  # 使用json参数传递JSON数据  
#         if response.status_code == 200:  # 检查响应状态码是否为200（成功）  
#             response_data = response.json()  # 解析响应内容为Python字典  
#             print('登录成功')
#             token = response_data['data']['token']  # 提取token的值  
#             return token  
#         else:  
#             print("登录失败")  
#             return None


#     def set_password_code(token):
#         url = 'http://dev.nexusftx.com:8801/uc/mobile/update/password/code'
#         headers={'X-Auth-Token':token}
#         response = requests.post(url,headers=headers)
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#         print(response.text)
#         return response.text  
    
#     def set_password(token):
#         url='http://dev.nexusftx.com:8801/uc/approve/update/password'
#         headers={'X-Auth-Token':token}
#         data={'oldPassword':'Wyt123456','newPassword':'Wyt1234567', 'confirmPassword':'Wyt1234567','code':'999999','verify':'0'}
#         response = requests.post(url, data=data,headers=headers)  
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#         return response.text  
        
#     def fund_password_code(token):
#         url='http://dev.nexusftx.com:8801/uc/mobile/set/fund/password/code'
#         headers={'X-Auth-Token':token}
#         response=requests.get(url,headers=headers)
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#         return response.text

#     def fund_password(token):
#         url='http://dev.nexusftx.com:8801/uc/approve/transaction/password'
#         headers={'X-Auth-Token':token}
#         data={"jyPassword": "536661","code":"999999"}
#         response=requests.post(url,headers=headers,data=data)
#         response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#         return response.text
    

# 使用这两个函数  
# phone = phon_test.random_phone()  
# username =phon_test.generate_random_username()  
# print(phon_test.send_sms_code())
# print(phon_test.register())  # 注册操作
# # # print(test.login())
# print(test.login())
# print(test.set_password_code())
# print(test.set_password())


# phone=random_phone()
# username,phone=register_user()
# print(username,phone)
# login_response = phon_test.login(phone)  
# token=login_response

# print(phon_test.set_password_code(token))
# print(phon_test.set_password(token))
# # print(phon_test.fund_password_code(token))
# # print(phon_test.fund_password(token))





class PhonTest:  
    def __init__(self):  
        self.username = None  
        self.phone = None  
        self.password = 'Wyt123456'  
        self.token = None  
      
    def random_phone():    
        second = random.choice([3, 4, 5, 7, 8])    
        third = {    
            3: random.randint(0, 9),    
            4: random.choice([5, 7, 9]),    
            5: random.choice([i for i in range(10) if i != 4]),    
            7: random.choice([i for i in range(10) if i not in [4, 9]]),    
            8: random.randint(0, 9),    
        }[second]    
        suffix = random.randint(9999999, 100000000)    
        phone = "1{}{}{}".format(second, third, suffix)    
        return phone  
      
    def generate_random_username(self):    
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))    
        random_digits = ''.join(random.choices(string.digits, k=3))    
        self.username = "Wyt123" + random_letters + random_digits    
        return self.username  
      
    def send_sms_code(self):    
        url = 'http://13.215.67.65:8801/uc/mobile/code'    
        data = {"phone": self.phone, "country": "阿富汗"}    
        response = requests.post(url, data=data)    
        response.encoding = 'utf-8'    
        return response.text    
      
    def register(self):    
        url = 'http://13.215.67.65:8801/uc/register/phone'    
        data = {    
            'phone': self.phone,  
            'username': self.username,    
            'password': self.password,    
            'captchaVerification': 'captchaVerification',    
            "country": "阿富汗",      
            "code": "999999",  
            "promotion": ""  
        }    
        response = requests.post(url, data=data)    
        response.encoding = 'utf-8'    
        print(self.phone, self.username)     
        return response.text     
      
    def login(self):    
        url = 'http://dev.nexusftx.com:8801/uc/login'    
        data = {    
            "username": self.generate_random_username(),     
            "password": self.password,    
            "captchaVerification": "mockCaptchaVerification"    
        }    
        response = requests.post(url, data=data)    
        if response.status_code == 200:    
            response_data = response.json()    
            print('登录成功')  
            self.token = response_data['data']['token']    
            return self.token    
        else:    
            print("登录失败")    
            return None  
    @staticmethod
    def send_request(method, url, headers=None, data=None):  
        session = requests.Session()  
        response = session.request(method, url, headers=headers, data=data)  
        response.encoding = 'utf-8'  
        return response   
     
    def set_password_code(token):  
        url = 'http://dev.nexusftx.com:8801/uc/mobile/update/password/code'  
        headers = {'X-Auth-Token': token}  
        response = send_request('POST', url, headers=headers)  
        print(response.text)  
        return response  
    
    def set_password(token):  
        url = 'http://dev.nexusftx.com:8801/uc/approve/update/password'  
        headers = {'X-Auth-Token': token}  
        data = {'oldPassword': 'Wyt123456', 'newPassword': 'Wyt1234567', 'confirmPassword': 'Wyt1234567', 'code': '999999', 'verify': '0'}  
        return send_request('POST', url,    headers=headers, data=data)  
    
    def fund_password_code(token):  
        url = 'http://dev.nexusftx.com:8801/uc/mobile/set/fund/password/code'  
        headers = {'X-Auth-Token': token}  
        return send_request('GET', url, headers=headers)  
    
    def fund_password(token):  
        url = 'http://dev.nexusftx.com:8801/uc/approve/transaction/password'  
        headers = {'X-Auth-Token': token}  
        data = {"jyPassword": "536661", "code": "999999"}  
        return send_request('POST', url, headers=headers, data=data)
    


phone=PhonTest.random_phone()
username,phone=PhonTest.register_user()
print(username,phone)