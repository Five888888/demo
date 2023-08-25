# 导包
from api.minilogin import miniLoginAPI
from api.auth import AuthAPI


# 创建测试类
class TestLoginAccountIdForTest:
    # 初始化
    token = None

    # 前置处理
    def setup(self):
        # 实例化接口对象
        self.auth_api = AuthAPI()

    # 后置处理
    def teardown(self):
        pass

    # 2.获取用户基本信息(App)
    def test_user_info_app(self, get_token):
        response = self.auth_api.user_info_app(token=get_token)
        print(response.json())

    # 3.获取用户基本信息(wxliteapp)
    def test_user_info_wxliteapp(self, get_token):
        response = self.auth_api.user_info_wxliteapp(token=get_token)
        print(response.json())
