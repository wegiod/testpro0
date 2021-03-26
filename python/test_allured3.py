# -*- coding: utf-8 -*-
# @Time      :2021/3/25 10:43 上午
# @Author    :jxd
# @File      :test_allured3.py
import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

# 添加html的代码块
def test_attach_html():
    allure.attach("<body>这是一段html</body>","html测试块",attachment_type=allure.attachment_type.HTML)

# 添加图片
def test_attach_photo():
    allure.attach.file("/Users/giod/PycharmProjects/testpro0/python/WechatIMG539.jpg"
                  ,name="这是一个图片",attachment_type=allure.attachment_type.JPG)

