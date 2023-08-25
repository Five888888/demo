import allure
import pytest
import os
from api.minilogin import miniLoginAPI
from common.colorlog import logger
from common.read_data import data


accountId = "1685169526981435393"
pwd = "2H83s(x"

testapi = miniLoginAPI()

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


cesbiz_data = get_data("cesbiz_data.yml")


@pytest.fixture(scope="session")
@allure.step("登录获取token")
def get_token():
    res = testapi.login(
        {"accountId": accountId, "pwd": pwd})
    logger.info("测试数据：【{}】".format(res.json()))
    token = "Bearer " + (res.json().get("data")).get("token")
    logger.info("token：==>> {}】".format(token))
    return token
