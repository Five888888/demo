# 方法：get
#
# 登录：
# 地址：config.BASE_URL
# 方法：Post
# 请求数据：
# GET请求的请求参数是直接放在URL中的
# 使用参数params

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的、接口方法被调用时需要返回对应的响应结果


# 导包
import requests
import config


# 创建接口类

class miniLoginAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_login = config.BASE_URL + "/api/auth/login/accountId-for-test"

    def login(self, test_data):
        return requests.get(url=self.url_login, params=test_data)
