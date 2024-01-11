import os
import unittest
from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest 
from common.mylogger import log
from common.constant import DATA_DIR
from common.conifg import myconf
from common.text_replace import data_replace
from common.common_google import token_generator


# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")
@ddt
class UnBindGoogleTestCase(unittest.TestCase):
    """解绑谷歌验证器"""

    excel = ReadExcel(data_file_path, 'unbindgoogle')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    def setUp(self):
        google=token_generator()
        token_code=google.run_registration_process()
        self.token=token_code
        print(self.token)
        self.secret=google.secret
        self.codes=google.codes
        google.bind_google()
        
    @data(*cases)
    def test_case_unbind_google(self, case):
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

        # # 替换动态化的参数
        case.data = case.data.replace("*code*", self.codes)
        case.data = case.data.replace("*secret*", self.secret)
        print(case.data)

        # 第二步：发送请求到接口，获取结果   
        #其他用例
        log.info('正在请求地址{}'.format(url))
        headers={'X-Auth-Token':self.token}
        response = self.http.request(method=method, url=url, data=eval(case.data),headers=headers)
        response.encoding='utf-8'
        # 获取返回的内容
        res = response.json()
        # 第三步：比对预期结果和实际结果，断言用例是否通过
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