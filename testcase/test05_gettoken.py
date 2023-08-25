# # 导包
# from api.minilogin import miniLoginAPI
#
#
# # 创建测试类
# class TestgetTokenAPI:
#     # 初始化
#     token = None
#
#     # 前置处理
#     def setup(self):
#         # 实例化接口对象
#         self.login_api = miniLoginAPI()
#
#     # 后置处理
#     def teardown(self):
#         pass
#
#     # 1.登陆成功
#     def test_gettoken(self):
#         # 登录
#         login_data = {
#             "accountId": "1685169526981435393",
#             "pwd": "2H83s(x"
#         }
#         response = self.login_api.login(test_data=login_data)
#         # 断言响应状态码为200
#         assert 200 == response.status_code
#         # 断言响应数据包含'成功'
#         #assert '成功' in response.text
#         # 断言响应json数据中status值
#         assert 200 == response.json().get("status")
#
#     # 2.登录失败