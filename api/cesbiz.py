# 接口封装

# 导包
import requests
import config

# 创建接口类
class CesbizAPI:
    # 初始化
    def __init__(self):
        self.url_charge_free = config.BASE_URL + "/api/ces/biz/charge/fee"

        self.url_qrcode = config.BASE_URL + "/api/ces/biz/qrcode"

        self.url_station = config.BASE_URL + "/api/ces/biz/station"

        self.url_appointment = config.BASE_URL + "/api/ces/biz/appointment"

        self.url_appointment_start = config.BASE_URL + "/api/ces/biz/appointment/start"

        self.url_appointment_stop = config.BASE_URL + "/api/ces/biz/appointment/stop"

        self.url_charge = config.BASE_URL + "/api/ces/biz/charge"

        self.url_charge_list = config.BASE_URL + "/api/ces/biz/charge/list"

        self.url_charge_start = config.BASE_URL + "/api/ces/biz/charge/start"

        self.url_charge_statistics = config.BASE_URL + "/api/ces/biz/charge/statistics"


    # 查询充电枪
    def qrcode(self, token, test_data):
        return requests.get(url=self.url_qrcode, headers={"Authorization": token}, params=test_data)

    # 站点详情
    def station(self, token, test_data):
        return requests.get(url=self.url_station, headers={"Authorization": token}, params=test_data)

    # 查询预约订单
    def appointment(self, token, test_data):
        return requests.get(url=self.url_appointment, headers={"Authorization": token}, params=test_data)

    # 开始预约  post请求使用param传参
    def appointment_start(self, token, test_data):
        return requests.post(url=self.url_appointment_start, headers={"Authorization": token}, data=test_data)

    # 结束预约
    def appointment_stop(self, token, test_data):
        return requests.post(url=self.url_appointment_stop, headers={"Authorization": token}, data=test_data)

    # 查询充电订单
    def charge(self, token, test_data):
        return requests.get(url=self.url_charge, headers={"Authorization": token}, params=test_data)

    # 查询运营商电价
    def charge_free(self, token, test_data):
        return requests.get(url=self.url_charge_free, headers={"Authorization": token}, params=test_data)

    # 查询充电订单list
    def charge_list(self, token, test_data):
        return requests.get(url=self.url_charge_list, headers={"Authorization": token}, params=test_data)

    # 启动充电
    def charge_start(self, token, test_data):
        return requests.post(url=self.url_charge_start, headers={"Authorization": token}, data=test_data)

    # 充电订单金额与度数统计
    def charge_statistics(self, token, test_data):
        return requests.get(url=self.url_charge_statistics, headers={"Authorization": token}, params=test_data)