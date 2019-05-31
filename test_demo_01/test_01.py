# -*- coding: utf-8 -*-
import allure


class Test01:
    """
    Allure Features - steps
    """

    # 案例一
    def test_case_01(self):
        self.step_1()

    @allure.step
    def step_1(self):
        assert 1 == 1
        self.step_01()

    @allure.step
    def step_01(self):
        assert 11 == 11
        self.step_011()

    @allure.step
    def step_011(self):
        assert 111 == 111

    # 案例二
    def test_case_02(self):
        self.step_2(1, 2, key=None)
        self.step_2(1, 2, 3, key=None)
        self.step_2(1, 2, key="other thing")

    @allure.step('''
    带有注释的 step，可以打印参数信息。
    
    位置参数：{1}, {2}
    
    关键字参数：{key}
    ''')
    def step_2(self, *arg1, key=None):
        pass

    # 案例三
    def test_case_03(self, initial):
        assert 1 == 1
