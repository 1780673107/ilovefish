import random,string
import requests
import urllib
from urllib.parse import urlparse, parse_qs, urlunparse
class EmailGenerator():
    def __init__(self):
      self.emails = self.generate_random_email()
      self.send_email_code=self.send_email_code()
      self.reg_email_code=self.reg_email_code()
      self.url=self.update_url_email()

    def generate_random_email(self):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com','qq.com','163.com']  # 可以根据需要添加更多的域名
        username_length = random.randint(5, 10)
        # 生成随机用户名
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        # 随机选择域名
        domain = random.choice(domains)
        # 组合成邮箱地址
        email = f'{username}@{domain}'
        return email

    def send_email_code(self):
        url=self.update_url_email
        res=requests.get(url)
        return res.text

    def reg_email_code(self):
        url=self.update_url_email
        res=requests.get(url)
        return res.text

    def update_url_email(self):
        # 解析URL以获取查询参数部分
        parsed_url = urlparse('http://13.215.67.65:8801/uc/mockData/reg_email_code?email=new1_use1r@example.com')

        # 更新或创建email参数
        params = parse_qs(parsed_url.query)
        params['email'] = [self.emails]

        # 将新的查询参数序列化回字符串
        updated_query = urllib.parse.urlencode(params, doseq=True)  # 注意这里已正确导入了urllib.parse

        # 使用更新后的查询参数构造新的URL
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, updated_query, parsed_url.fragment))

        return new_url

  # # 使用函数
  # original_url = 'http://dev.nexuspb.com:8801/uc/verify/email/register?email=1231232%40qq.com&country=%E9%98%BF%E5%AF%8C%E6%B1%97'
  # new_email = 'new_use1r@example.com'

a=EmailGenerator()
print(a.update_url_email())
print(a.send_email_code())
print(a.reg_email_code())
