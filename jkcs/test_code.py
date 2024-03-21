import xToolkit
import requests
import pytest
import os
import allure_pytest


all_Case=xToolkit.xfile.read("test.xls").excel_to_dict(sheet=0)
print("所有信息：",all_Case)


@pytest.mark.parametrize("case",all_Case)
def test_api(case):
    response=requests.request(url=eval(case["接口URL"]),
                              method=case["请求方式"],
                              json=eval(case["URL参数"]) ,
                              headers=eval(case["参数类型"]) )

    assert response.status_code==case["预期状态码"],"测试不通过，状态码错误"


if __name__ == '__main__':
    pytest.main(['--alluredir=allure-results'])
    os.system(r"allure generate allure-results -c ")