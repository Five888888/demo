# # 导包
# from api.login import LoginAPI
#
#
# # 创建测试类
# class TestContractBusiness:
#     # 前置处理
#     def setup(self):
#         # 实例化接口对象
#         self.login_api = LoginAPI()
#
#     # 后置处理
#     def teardown(self):
#         pass
#
#     # 1.登陆成功
#     def test_login_success(self):
#         # 获取验证码
#         res_v = self.login_api.get_verify_code()
#         print(res_v.status_code)
#         print(res_v.json())
#         # 打印uuid数据
#         print(res_v.json().get("uuid"))
#
#         # 登录
#         login_data = {
#             "username": "admin",
#             "password": "HM_2023_test",
#             "code": 2,
#             "uuid": res_v.json().get("uuid")
#         }
#         res_l = self.login_api.login(test_data=login_data)
#         print(res_l.status_code)
#         print(res_l.json())
