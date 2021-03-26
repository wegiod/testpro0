# -*- coding: utf-8 -*-
# @Time      :2021/3/18 10:59 上午
# @Author    :jxd
# @File      :test_data.py
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("测试环境")
            print("测试环境的ip是：",env["test"])
        elif "dev" in env:
            print("开发环境")
            print("开发环境的ip是：",env["dev"])
    # def test_yaml(self):
    #     print(yaml.safe_load(open("./env.yaml")))


