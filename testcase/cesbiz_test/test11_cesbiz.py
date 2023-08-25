# 导包
import allure
import pytest

from api.cesbiz import CesbizAPI
from common.colorlog import logger
from testcase.conftest import cesbiz_data


@allure.epic("充电、预约")
@allure.feature("充电、预约或涉及流程业务接口")
class TestCesBiz:
    # 初始化
    token = None

    # 前置处理
    def setup(self):
        # 实例化接口对象
        self.cesbiz_api = CesbizAPI()

    @allure.story("查询预约订单")
    @allure.description("该用例是针对查询预约订单接口的测试")
    @allure.title("测试数据：{data}")
    @allure.issue("https://www.cnblogs.com/wintest", name="BUG号：123")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.parametrize("data", cesbiz_data["test_appointment_info"])
    def test01_appointment(self, get_token, data):
        response = self.cesbiz_api.appointment(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("开始预约")
    @allure.description("该用例是针对开始预约接口的测试")
    @allure.title("测试数据：{data}")
    @pytest.mark.parametrize("data", cesbiz_data["test_appointment_start_info"])
    def test02_appointment_start(self, get_token, data):
        response = self.cesbiz_api.appointment_start(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("结束预约")
    @allure.description("该用例是针对结束预约接口的测试")
    @allure.title("测试数据：{data}")
    @pytest.mark.parametrize("data", cesbiz_data["test_appointment_stop_info"])
    def test03_appointment_stop(self, get_token, data):
        response = self.cesbiz_api.appointment_stop(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("查询运营商电价")
    @allure.description("该用例是针对查询运营商电价接口的测试")
    @allure.title("测试数据：{data}")
    @pytest.mark.parametrize("data", cesbiz_data["test_charge_free_info"])
    def test04_charge_free(self, get_token, data):
        response = self.cesbiz_api.charge_free(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("查询充电订单")
    @allure.description("该用例是针对查询充电订单接口的测试")
    @allure.title("查询充电订单接口")
    @pytest.mark.parametrize("data", cesbiz_data["test_charget_info"])
    def test05_charget(self, get_token, data):
        response = self.cesbiz_api.charge(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("查询充电订单list")
    @allure.description("该用例是针对查询充电订单list接口的测试")
    @allure.title("查询充电订单list接口")
    @pytest.mark.parametrize("data", cesbiz_data["test_charge_list_info"])
    def test06_charge_list(self, get_token, data):
        response = self.cesbiz_api.charge_list(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    # @allure.feature("启动充电")
    # def test_charge_start(self):
    #     data = {
    #         ""
    #     }
    #     response = self.cesbiz_api.charge_start(token=TestCesBiz.token, test_data=data)
    #     print(response.status_code)
    #     print(response.json())

    @allure.story("充电订单金额与度数统计")
    @allure.description("该用例是针对充电订单金额与度数统计接口的测试")
    @allure.title("充电订单金额与度数统计接口")
    @pytest.mark.parametrize("data", cesbiz_data["test_charge_statistics_info"])
    def test07_charge_statistics(self, get_token, data):
        response = self.cesbiz_api.charge_statistics(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("查询充电枪")
    @allure.description("该用例是针对查询充电枪接口的测试")
    @allure.title("查询充电枪接口")
    @pytest.mark.parametrize("data", cesbiz_data["test_qrcode_info"])
    def test08_qrcode(self, get_token, data):
        response = self.cesbiz_api.qrcode(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200

    @allure.story("站点详情")
    @allure.description("该用例是针对站点详情接口的测试")
    @allure.title("站点详情接口")
    @pytest.mark.parametrize("data", cesbiz_data["test_station_info"])
    def test09_station(self, get_token, data):
        response = self.cesbiz_api.station(token=get_token, test_data=data)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(200, response.status_code))
        logger.info("测试数据：【{}】".format(response.json()))
        assert response.status_code == 200
