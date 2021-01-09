"""
    @file: test_api.py
    @Author: Shieh
    @Date: 2021/1/3 18:23
    @Description: 
"""
import pytest
from api.api import Api
from tools.common_assert import common_assert
from tools.operation_excel import OperationExcel


class TestApi:
    tool = OperationExcel("api.xlsx")
    tool.read_excel()

    @pytest.mark.parametrize("case", tool.read_json())
    def test_login(self, case):
        try:
            re = Api(case).run_method()
            # 断言
            common_assert(re, case)
            # 将执行结果写入Excel
            TestApi.tool.write_excel(case.get("x_y"), "Success！")
        except Exception as e:
            TestApi.tool.write_excel(case.get("x_y"), "Failed！ Reason: {}".format(e))
            raise
