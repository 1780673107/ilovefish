



import requests  
import random  
import json


def send_email_code(email):  
    url = 'http://dev.nexusftx.com:8801/uc/reg/email/code'  
    data = {"email": email}  
    response = requests.post(url, data=data)  
    response.encoding = 'utf-8'  
    return response.text  


def generate_random_username():
    user_num = random.randint(0, 999999)
    return f"Wyt{user_num}"

def register_with_email(email):  
    """  
    使用邮箱注册。  
    参数：邮箱地址。  
    """  
    url = "http://dev.nexusftx.com:8801/uc/mockData/reg_email_code"    
    params = {"email": email}    
    
    response = requests.get(url, params=params)    
    
    if response.status_code == 200:    
        try:    
            data_response = json.loads(response.text)    
            data = data_response['data']    
            print("请求成功")       
            # 在此处，你可以使用'data'进行下一个接口的调用    
        except KeyError:    
            print("响应中缺少'data'键")    
    else:    
        print("请求失败，状态码：", response.status_code)
    print(response.text)
    # return data


# def send_email(email,code):
#     url = 'http://dev.nexusftx.com:8801/uc/register/email'  
#     data =  { 'email': email,
#     'username':username,
#     'password': 'Wyt123456',
#     'promotion': '',
#     'code': code
#     } 
#     response = requests.post(url, data=data)  
#     response.encoding = 'utf-8'  # 注意这里应该使用 encoding，而不是 encode  
#     return response.text  


# username= generate_random_username()
email = '555534111@qq.com'
# register_with_email(email)

print(send_email_code(email))
print(register_with_email(email))
# print(send_email(email,a))
# print(send_email_code(email))


