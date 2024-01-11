import requests
import time
import random

# 随机生成手机号码
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
    return "1{}{}{}".format(second, third, suffix)

# 发送短信验证码
def send_sms_verification_code(phone):
    sms_url = "http://13.215.67.65:8801/uc/mobile/code"  
    sms_params = {"phone": phone,
                  "country":'阿富汗'}
    
    response=requests.post(sms_url, params=sms_params)
    return response.text
    

# 注册用户
def register(phone, username, password):
    code = send_sms_verification_code(phone)  # 发送短信并获取验证码
    register_url1='http://13.215.67.65:8801/uc/register/phone'
    register_url = "http://127.0.0.1:6001/uc/register/phone"  # 替换为实际的URL
    register_params = {
        "phone": phone,
        "country": "阿富汗",
        "username": username,
        "password": password,
        "promotion": "",
        "code": '999999'
    }
    
    resp = requests.post(register_url1, params=register_params)
    print(resp.text)

# 生成随机用户名
def generate_random_username():
    user_num = random.randint(0, 999999)
    return f"Wyt123{user_num}"

# 注册用户并返回手机号和用户名
def register_user():
    phone = random_phone()
    username = generate_random_username()
    register(phone, username, "Wyt123456")
    return phone, username








# phone=random_phone()
# send_sms_verification_code(phone)
# phone,username=register_user()
# print(phone,username)