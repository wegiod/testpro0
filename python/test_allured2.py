# -*- coding: utf-8 -*-
# @Time      :2021/3/20 7:23 下午
# @Author    :jxd
# @File      :test_allured2.py

import allure

#给测试结果增加一个链接
import pytest


@allure.link("http://www.baidu.com",name="链接")
def test_with_link2():
    print("这是一条加了链接的测试")
    pass

#给测试结果增加一个链接
TEST_CASE_LINK  = 'http://www.baidu.com'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_link():
    print("这是一条测试用例的链接，链接到测试报告里面")
    pass


#102是bug编号
@allure.issue('102','这是一个用例描述')
def test_with_link3():
    pass
# --allure-link-pattern=issue:http:www.baidu.com

@allure.severity(allure.severity_level.NORMAL)
class TestClass(object):
    def test_with_link4(self):
        print("这是4")
        pass
    @allure.severity(allure.severity_level.CRITICAL)
    def test_with_link5(self):
        print("这是5")
        pass

    def test_with_link6(self):
        print("这是6")
        pass

    def test_with_link7(self):
        print("这是7")
        pass
@allure.severity(allure.severity_level.NORMAL)
def test_with_link8():
    print("这是8")
    pass

def test_with_link9():
    print("这是9")
    pass

if __name__ == '__main__':
    pytest.main()

