# -*- coding: utf-8 -*-
import allure


class Test01:
    """
    Allure Tags - Severity markers
    """

    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_01(self):
        assert True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_02(self):
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_case_03(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_case_04(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_case_05(self):
        assert True
