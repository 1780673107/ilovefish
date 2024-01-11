import os
import unittest
import json
from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest 
from common.mylogger import log
from common.constant import DATA_DIR
# from common.do_mysql import ReadSQL
import requests
from common.conifg import myconf
from common.text_replace import data_replace
from common.regis import send_sms_verification_code,random_phone,generate_random_username
import time
# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")




@ddt
class RegisterTestCase(unittest.TestCase):  
    """注册接口"""  
    excel = ReadExcel(data_file_path, 'register')  
    cases = excel.read_data_obj()  
    http = HTTPRequest()
    


        
    
    def setUp(self):
        # 执行前置操作
        self.phone=random_phone()
        username = generate_random_username()
        self.SMScode(self.phone)
        self.username = username

    def SMScode(self,phone):
        url1 = 'http://13.215.67.65:8801/uc/mobile/code'          
        data1 = {"phone":self.phone, "country": "阿富汗"}       
        response = requests.post( url1, data1) #     
        response.encoding = 'utf-8'   
        response.raise_for_status()
        print(response.text)
        print(phone)

    
    @data(*cases)
    def test_register(self, case):
        # 登录接口用例执行的逻辑
        # 第一步：准备测试用例数据
        url = myconf.get('url','url1')+case.url
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        # 替换用例参数
        # 替换配置文件夹中固定的参数
        data = data_replace(case.data)
        print(data)
        
        
        # 替换动态化的参数
        case.data = case.data.replace("*phone*",self.phone)
        case.data = case.data.replace("*username*", self.username)
        print(case.data)
        # 第二步：发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=case.method, url=url, data=eval(case.data))
        response.encoding='utf-8'
        # 获取返回的内容
        print(response.text)
        print(url)
        print(self.phone)
        res = response.json()  
        print(res)
        if case.title == '密码为空' or case.title=='密码不符合复杂度要求' or case.title==' 密码长度不足5位':
            try:
                self.assertEqual(excepted["code"], res["code"])
                # self.assertEqual(excepted["message"], res["message"])
            except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
                self.excel.write_data(row=row, column=8, value='未通过')
                log.debug('{}，该条用例执行未通过'.format(case.title))
                raise e
            else:
            # 测试用例执行通过
                self.excel.write_data(row=row, column=8, value='通过')
                log.debug('{}，该条用例执行通过'.format(case.title))
            
        else:
            try:
                self.assertEqual(excepted, res)
            except AssertionError as e:
                # 测试用例未通过
                # 获取当前用例所在行
                self.excel.write_data(row=row, column=8, value='未通过')
                log.debug('{}，该条用例执行未通过'.format(case.title))
                raise e
            else:
                # 测试用例执行通过
                self.excel.write_data(row=row, column=8, value='通过')
                log.debug('{}，该条用例执行通过'.format(case.title))



# phone=random_phone()
# def SMScode():
#     url = 'http://13.215.67.65:8801/uc/mobile/code'          
#     data1 = {"phone":phone, "country": "阿富汗"}       
#     response = requests.post( url, data1) #     
#     response.encoding = 'utf-8'   
#     print(phone) 
#     print(response.text) 
#     return phone

# class EnvData:
#     pass


# @ddt
# class RegisterTestCase(unittest.TestCase):  
#     """注册接口"""  
#     excel = ReadExcel(data_file_path, 'register')  
#     cases = excel.read_data_obj()  
#     http = HTTPRequest()  
#     username = generate_random_username()
#     @classmethod
#     def setUpClass(cls) -> None:
#         # 执行前置操作
#         phone = SMScode()
#         # 将data绑定到全局变量类的类属性上
#         EnvData.phone = phone
#         # 将data绑定到当前类的类属性上
#         cls.phone = phone
#         EnvData.phone=cls.phone
#     # def test_something(self):
#     #     print('执行测试')
#     #     # 获取前置方法中产生的数据
#     #     # 从全局变量中获取
#     #     print(EnvData.phone)
#     #     # 从当前用例的类属性中获取
#     #     print(self.__class__.phone)
#     #     # 如果当前用例对象没有同名对象属性，也可以直接从对象属性中获取
#     #     print(self.phone)
    
#     @data(*cases)
#     def test_register(self, case):
#         # 登录接口用例执行的逻辑
#         # 第一步：准备测试用例数据
#         url = myconf.get('url','url1')+case.url
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#         # 替换用例参数
#         # 替换配置文件夹中固定的参数
#         data = data_replace(case.data)
#         print(data)

        
#         # 替换动态化的参数
#         case.data = case.data.replace("*phone*",EnvData.phone)
#         case.data = case.data.replace("*username*", self.username)
#         print(case.data)
#         # 第二步：发送请求到接口，获取结果
#         log.info('正在请求地址{}'.format(url))
#         response = self.http.request(method=method, url=url, data=eval(data))
#         response.encoding='utf-8'
#         # 获取返回的内容
#         print(response.text)
#         print(url)
#         print(phone)
#         res = response.json()  
#         print(res)
#         if case.title == '正常登录成功' :
#             try:
#                 self.assertEqual(excepted["code"], res["code"])
#                 self.assertEqual(excepted["message"], res["message"])
#             except AssertionError as e:
#             # 测试用例未通过
#             # 获取当前用例所在行
#                 self.excel.write_data(row=row, column=8, value='未通过')
#                 log.debug('{}，该条用例执行未通过'.format(case.title))
#                 raise e
#             else:
#             # 测试用例执行通过
#                 self.excel.write_data(row=row, column=8, value='通过')
#                 log.debug('{}，该条用例执行通过'.format(case.title))
            
#         else:
#             try:
#                 self.assertEqual(excepted, res)
#             except AssertionError as e:
#                 # 测试用例未通过
#                 # 获取当前用例所在行
#                 self.excel.write_data(row=row, column=8, value='未通过')
#                 log.debug('{}，该条用例执行未通过'.format(case.title))
#                 raise e
#             else:
#                 # 测试用例执行通过
#                 self.excel.write_data(row=row, column=8, value='通过')
#                 log.debug('{}，该条用例执行通过'.format(case.title))


    # @data(*cases)
    # def test_register(self, case):
    #     # 登录接口用例执行的逻辑
    #     # 第一步：准备测试用例数据
    #     url = myconf.get('url','url1')+case.url
    #     method = case.method
    #     excepted = eval(case.excepted)
    #     row = case.case_id + 1
    #     # 替换用例参数
    #     # 替换配置文件夹中固定的参数
    #     data = data_replace(case.data)
    #     print(data)

    
    #     # 替换动态化的参数
    #     case.data = case.data.replace("*phone*", self.phone)
    #     case.data = case.data.replace("*username*", self.username)
    #     print(case.data)
    #     # 第二步：发送请求到接口，获取结果
    #     log.info('正在请求地址{}'.format(url))
    #     response = self.http.request(method=method, url=url, data=eval(data))
    #     response.encoding='utf-8'
    #     # 获取返回的内容
    #     print(response.text)
    #     print(case.url)
    #     print(url)
    #     res = response.json()  
    #     print(res)
    #     if case.title == '正常登录成功' :
    #         try:
    #             self.assertEqual(excepted["code"], res["code"])
    #             self.assertEqual(excepted["message"], res["message"])
    #         except AssertionError as e:
    #         # 测试用例未通过
    #         # 获取当前用例所在行
    #             self.excel.write_data(row=row, column=8, value='未通过')
    #             log.debug('{}，该条用例执行未通过'.format(case.title))
    #             raise e
    #         else:
    #         # 测试用例执行通过
    #             self.excel.write_data(row=row, column=8, value='通过')
    #             log.debug('{}，该条用例执行通过'.format(case.title))
            
    #     else:
    #         try:
    #             self.assertEqual(excepted, res)
    #         except AssertionError as e:
    #             # 测试用例未通过
    #             # 获取当前用例所在行
    #             self.excel.write_data(row=row, column=8, value='未通过')
    #             log.debug('{}，该条用例执行未通过'.format(case.title))
    #             raise e
    #         else:
    #             # 测试用例执行通过
    #             self.excel.write_data(row=row, column=8, value='通过')
    #             log.debug('{}，该条用例执行通过'.format(case.title))










    




