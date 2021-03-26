# -*- coding: utf-8 -*-
# @Time      :2021/3/18 4:29 下午
# @Author    :jxd
# @File      :test_allured.py
import pytest
import allure

#标注测试模块
@allure.feature("登录模块")
class TestLingo():
    @allure.story("登录成功")
    def test_success(self):
        """this test succeeds"""
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_failure(self):
        """this test fails"""
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("用户名缺失")
    def test_skip(self):
        """this test is skipped"""
        # pytest.skip('for a reason!')
        print("用户名缺失")
        pass
    #标注测试功能
    @allure.story("密码缺失")
    def test_broken(self):
        #标注测试步骤
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        with allure.step("点击登录会后登录失败"):
            assert "1" == 1
            print("登录失败")

        pass








