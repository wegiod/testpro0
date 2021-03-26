# -*- coding: utf-8 -*-
# @Time      :2021/3/25 2:54 下午
# @Author    :jxd
# @File      :test_calc.py
import pytest

from test_pytest.core.calc import Calc



# class TestCalc:
#
#     def setup_class(self):
#         self.calc = Calc()
#     @pytest.mark.parametrize('a,b,c', [
#         [1, 2, 2],
#         [-1, -1, 1],
#         [-1, 1, -1]
#     ])
#     def test_mul(self,a, b, c):
#         assert self.calc.mul(a, b) == c

class Testmul:
    #初始化
    def setup_class(self):
        self.calc = Calc()
    #参数化
    @pytest.mark.parametrize('a,b,c',[
        [1,2,2],
        [0.5,0.5,0.25],
        [-1,1,-1],
        [0,1,0],
        [0,0,0]
    ])
    #执行测试用例
    def test_mul(self,a,b,c):
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,c',[
        [1,2,0.5],
        [2,1,2],
        [0,1,0],
        [-1,1,-1],
        [10,3,3.3333333333333335],
        [0.2,0.1,2]
    ])
    def test_div(self,a,b,c):
        #判断是什么类型的错误，这里是除零的错误
        # with pytest.raises(ZeroDivisionError):
        assert self.calc.div(a,b) == c

    @pytest.mark.parametrize('a,b',[
        [1,0],
        [0.2,0],
        [-1,0]
    ])
    def test_div(self,a,b):
        #判断是什么类型的错误，这里是除零的错误
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a,b)







