
import re
from common.conifg import myconf


def data_replace(data):
    """替换动态参数"""
    while re.search(r'#(.+?)#',data):
        res = re.search(r'#(.+?)#',data)
        # 提取要替换的内容
        r_data = res.group()
        # 获取要替换的字段
        key = res.group(1)
        # 去配置文件中读取字段对应的数据
        value = myconf.get('data',key)
        # 进行替换
        data = re.sub(r_data,value,data)

    return data















if __name__ == '__main__':
    s2 = '{"mobilephone":"#phone#","pwd":"#pwd#","regname":"n123"}'
    data =data_replace(s2)
    print(data)







    #

    #
    # s3 = '{"mobilephone":"12333333","pwd":"1233","regname":"123"}'
    #
    # # 通过search方法进行匹配
    # # 判读是否有匹配到数据
    #
    #
    # while re.search(r'#(.+?)#', s2):
    #     res7 = re.search(r'#(.+?)#', s2)
    #     # 获取匹配到的内容
    #     r_data = res7.group()
    #     # 提取要替换的字段
    #     key = res7.group(1)
    #     # 通过提取的字段，去配置文件中读取对应的数据内容
    #     phone = myconf.get('data', key)
    #     # 进行替换操作
    #     s2 = re.sub(r_data, phone, s2)
    #
    #
    # print(s2)