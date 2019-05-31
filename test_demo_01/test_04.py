# -*- coding: utf-8 -*-
import allure
import pytest


class Test04:
    """
    Allure Features - titles
    """

    @allure.title('测试标题 by @allure.title')
    def test_case_01(self):
        assert True

    @allure.title('参数化测试标题：{param}')
    @pytest.mark.parametrize('param', ['title 1', 'title 2', 'title 3'])
    def test_case_02(self, param):
        print(param)
        assert True

    @allure.title('被替换的 title')
    def test_case_03(self):
        assert True
        allure.dynamic.title('替换装饰器中的 title')
