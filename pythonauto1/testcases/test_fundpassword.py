
import os
import random
import unittest
from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest
from common.mylogger import log
from common.constant import DATA_DIR
# from common.do_mysql import ReadSQL
from common.conifg import myconf
from common.text_replace import data_replace
from common.regis import send_sms_verification_code,random_phone
from common.regis2 import phone_test
import requests
# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")


@ddt
class FundPasswordTestCase(unittest.TestCase):
    """修改资金密码"""
    excel = ReadExcel(data_file_path, 'fundpassword')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    TestPhone=phone_test()
    # db = ReadSQL()
    def setUp(self):
        self.token=phone_test.get_login_token()
        print(self.token)
        # self.fund_password_code(self)
        self.response_text = self.fund_password_code()
    def fund_password_code(self):
        url='http://13.215.67.65:8801/uc/mobile/set/fund/password/code'
        # url='http://dev.nexuspb.com/:8801/uc/mobile/set/fund/password/code'
        
        headers={'X-Auth-Token':self.token}
        response=requests.get(url,headers=headers)
        response.encoding = 'utf-8'  
        return response.text

    @data(*cases)
    def test_case_fundpassword(self, case):
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
        # 随机生成手机号码
        # phone = self.random_phone
        # # 替换动态化的参数
        # case.data = case.data.replace("*phone*", phone)

        # 第二步：发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        headers={'X-Auth-Token':self.token}
        response = self.http.request(method=method, url=url, data=eval(data),headers=headers)
        response.encoding='utf-8'
        # 获取返回的内容
        res = response.json()
        # 第三步：比对预期结果和实际结果，断言用例是否通过
        if case.title == '1' :
            try:
                self.assertEqual(excepted["code"], res["code"])
                self.assertEqual(excepted["message"], res["message"])
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




