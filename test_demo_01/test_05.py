# -*- coding: utf-8 -*-
import allure
from allure_commons.types import LinkType


class Test04:
    """
    Allure Features - links
    """

    @allure.link('https://ide.codemao.cn')
    def test_case_01(self):
        assert True

    @allure.link('https://wood.codemao.cn', LinkType.LINK, 'Wood')
    def test_case_02(self):
        assert True

    @allure.issue('https://box.codemao.cn', 'Box')
    def test_case_03(self):
        assert True
