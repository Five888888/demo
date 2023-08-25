import pytest
from testcase.conftest import cesbiz_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return cesbiz_data.get(testcase_name)
