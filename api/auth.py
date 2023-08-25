# URL： BASE_URL
# 方法：Get
# 请求数据：
# 请求头：{ "Content-Type ":  " multipart/form-data ",  "Authorization":  "xxx " }
# 请求体：{" file " : 合同文件"}

# 接口信息： 新增合同： 地址：http://kdtx-test.itheima.net/api/contract 方法：Post 请求数据： 请求头：{ "Content-Type ":  "application/json ",
# "Authorization":  "xxx " } 请求体：{ "name": "测试888", "phone": "13612345678", "contractNo": "HT10012003", "subject":
# "6", "courseId": " 99", "channel": "0", "activityId": 77, "fileName": "xxx"}

# 导包
import requests
import config


# 创建接口类
class AuthAPI:
    # 初始化
    def __init__(self):
        self.url_user_info_app = config.BASE_URL + "/api/auth/user-info"

        self.url_user_info_wxliteapp = config.BASE_URL + "/api/auth/user-info"

    # 获取用户基本信息(App)
    def user_info_app(self, token):
        return requests.get(url=self.url_user_info_app, headers={"Authorization": token})

    # 获取用户基本信息(wxliteapp)
    def user_info_wxliteapp(self, token):
        return requests.get(url=self.url_user_info_wxliteapp, headers={"Authorization": token})
