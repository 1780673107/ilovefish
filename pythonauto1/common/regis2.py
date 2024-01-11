
import requests  
import random  
import string

class phone_test:  
    def __init__(self):  
        self.phone = self.random_phone()  
        self.username=self.generate_random_username()
        self.sms=self.send_sms_verification_code()
        
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
        sms_params = {"phone": self.phone, "country":'阿富汗'}  
        response = requests.post(sms_url, params=sms_params)  
        return response.text  
    

    def generate_random_username(self):  
        # 随机选择3个字母  
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))  
        # 随机选择3个数字  
        random_digits = ''.join(random.choices(string.digits, k=3))  
        # 组合用户名  
        self.username = "Wyt123" + random_letters + random_digits  
        return self.username

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
        response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
        return response.text 
    
    def login(self):  
        url = "http://13.215.67.65:8801/uc/login"    
        data = {  
            "username": self.phone,   
            "password": 'Wyt123456',  
            "captchaVerification":"mockCaptchaVerification"  
        }  
        response = requests.post(url, data)  
        response.encoding = 'utf-8'  
        response_json = response.json()    
        
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
    
    
    @staticmethod
    def get_login_token():  
        test_phone_instance = phone_test()    
        test_phone_instance.send_sms_verification_code()  
        test_phone_instance.register()  
        return test_phone_instance.login()



test_instance = phone_test() 
token_code=test_instance.get_login_token()

print(test_instance.get_login_token())