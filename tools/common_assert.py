"""
    @file: assert.py
    @Author: Shieh
    @Date: 2021/1/3 18:35
    @Description: 
"""


def common_assert(response, case):
    # 获取响应数据
    result = response.json()
    # 获取预期结果
    expect = case.get("expect")
    # 断言响应状态码
    assert response.status_code == expect.get("code"), "ERROR! Response code: {} Expect code: {}".format(
        response.status_code, expect.get("code"))
    # 断言 success
    assert result.get("success") == expect.get("result").get(
        "success"), "ERROR! Response success: {} Expect success: {}".format(result.get("success"),
                                                                            expect.get("result").get("success"))
    # 断言 code
    assert result.get("code") == expect.get("result").get("code"), "ERROR! Date code: {} Expect code: {}".format(
        result.get("code"), expect.get("result").get("code"))
    # 断言 message
    assert result.get("message") == expect.get("result").get(
        "message"), "ERROR! Response message: {} Expect message: {}".format(result.get("message"),
                                                                            expect.get("result").get("message"))
