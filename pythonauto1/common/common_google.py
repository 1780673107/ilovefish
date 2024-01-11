import random
import requests
import json
import string
import hmac, base64, struct, hashlib, time

class token_generator():
    def __init__(self):
        self.phone = self.random_phone()
        self.username = self.generate_random_username()
        self.token = self.run_registration_process()
        self.secret=self.google_create()
        self.codes=self.print_totp_token()

    def random_phone(self):  
        second = random.choice([3, 4, 5, 7, 8])  
        third = {  
            3: random.randint(0, 9),  
            4: random.choice([5, 7, 9]),  
            5: random.choice([i for i in range(10) if i != 4]),  
            7: random.choice([i for i in range(10) if i not in [4, 9]]),  
            8: random.randint(0, 9),  
        }[second]  
        suffix = random.randint(9999999, 100000000)  
        return "1{}{}{}".format(second, third, suffix)  
    
    def send_sms_verification_code(self):  
        sms_url = "http://13.215.67.65:8801/uc/mobile/code"    
        sms_params = {"phone": self.phone, "country": '阿富汗'}  
        response = requests.post(sms_url, params=sms_params)  
        return response.text  

    def generate_random_username(self):  
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))  
        random_digits = ''.join(random.choices(string.digits, k=3))  
        return "Wyt123" + random_letters + random_digits

    def register(self):  
        reg_url = 'http://13.215.67.65:8801/uc/register/phone'  
        data = {  
            'phone': self.phone,
            'username': self.username,  
            'password': "Wyt123456",  
            'captchaVerification': 'captchaVerification',  
            "country": "阿富汗",    
            "code": "999999",
            "promotion": ""
        }  
        response = requests.post(url=reg_url, data=data)  
        response.encoding = 'utf-8'
        return response.text 

    def login(self):  
        url = "http://13.215.67.65:8801/uc/login"    
        data = {  
            "username": self.phone,
            "password": 'Wyt123456',  
            "captchaVerification": "mockCaptchaVerification"  
        }  
        response = requests.post(url, data)  
        response.encoding = 'utf-8'  
        response_json = response.json()    
        
        if response_json.get('code') == 0 and response_json.get('message') == 'SUCCESS':  
            data = response_json.get('data')  
            if data:  
                token = data.get('token')  
                if token:  
                    self.token = token
                    return token  
                else:  
                    print("登录成功，但未返回token")  
            else:  
                print("登录成功，但未返回数据")  
        else:  
            print("登录失败:", response_json.get('message'))  
            
        return None
    """已绑定的账号直接登录"""
    def bind_login(self):
        url = "http://13.215.67.65:8801/uc/login"    
        data = {  
            "username": "15222222222",
            "password": 'Wyt123456',  
            "captchaVerification": "mockCaptchaVerification"  
        }  
        response = requests.post(url, data)  
        response.encoding = 'utf-8'  
        response_json = response.json()
      
    
        if response_json.get('code') == 0 and response_json.get('message') == 'SUCCESS':  
            data = response_json.get('data')  
            if data:  
                token = data.get('token')  
                if token:  
                    self.token = token
                    return token  
                else:  
                    print("登录成功，但未返回token")  
            else:  
                print("登录成功，但未返回数据")  
        else:  
            print("登录失败:", response_json.get('message'))  
            
        return None
        
    def run_registration_process(self):
        self.send_sms_verification_code()
        self.register()
        self.login()
        # registration_result = self.register()
        # if registration_result:
        #     print(self.phone,self.username)
        #     print("Registration Successful!")
        #     self.login()
        #     if self.token:
        #         print("Login Successful! Token:", self.token)
        #     else:
        #         print("Login Failed.")
        # else:
        #     print("Registration Failed.")
        return self.token
    


    
    def google_create(self):
        url = "http://13.215.67.65:8801/uc/verify/google/create" 

        headers = {"X-Auth-Token": self.token}
        response = requests.get(url=url, headers=headers)  
        secret=json.loads(response.text)
        secret=secret['data']['secret']
        return secret


    def get_hotp_token(self, intervals_no):
        key = base64.b32decode(self.secret, True)
        msg = struct.pack(">Q", intervals_no)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = ord(chr(h[19])) & 15
        h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
        return h

    def get_totp_token(self):
        return self.get_hotp_token(intervals_no=int(time.time()) // 30)
    
    def print_totp_token(self):
        value = self.get_totp_token()
        return (f"{str(value).zfill(6)}")
    
    def bind_google(self):
        url = "http://13.215.67.65:8801/uc/security/bind_google"
        data = {'codes': self.codes, "secret": self.secret}
        headers = {"X-Auth-Token": self.token}
        response = requests.post(url=url, headers=headers, data=data)
        return response.text

    def unbind_google(self):
        url = 'http://13.215.67.65:8801/uc/security/unbind_google'
        data = {"codes": self.codes, "password": 'Wyt123456'}
        headers = {"X-Auth-Token": self.token}
        response = requests.post(url=url, headers=headers, data=data)
        return response.text 
        

# 创建实例并执行注册流程
a = token_generator()

print(a.run_registration_process())
print(a.google_create())
print(a.print_totp_token())
print(a.bind_google())
print(a.unbind_google())