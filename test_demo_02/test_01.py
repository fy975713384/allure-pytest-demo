# -*- coding: utf-8 -*-
import allure


class Test01:
    """
    Allure Tags - BDD-style markers
    """

    @allure.epic('epic_1')
    def test_case_01(self):
        assert True

    @allure.story('story_1')
    def test_case_02(self):
        assert True

    @allure.feature('feature_1')
    def test_case_03(self):
        assert True
