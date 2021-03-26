# -*- coding: utf-8 -*-
# @Time      :2021/3/18 9:51 上午
# @Author    :jxd
# @File      :test_a.py
import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a',"a1"),
    (3,4),
    (5,6)
])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

@pytest.fixture()
def login():
    print("登录")
    username = 'giod'
    return username

class TestDemo:

    def test_a(self,login):
        print(f"a  {login}")

    def test_b(self):
        print("b")

    def test_c(self,login):
        print("c")





# 入口函数，使用python解释器运行pytest
if __name__ == '__main__':
    #指定运行文件
    pytest.main(['test_a.py::TestDemo','-v'])
