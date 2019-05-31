# -*- coding: utf-8 -*-
import allure


class Test02:
    """
    Allure Features - attachments
    """

    def test_case_01(self):
        self.attach_step_1()
        self.attach_step_2()
        self.attach_step_3()
        assert 1 == 1

    @allure.step
    def attach_step_1(self):
        allure.attach('<head></head><body> A test page </body>', '附件 HTML', allure.attachment_type.HTML,
                      extension='.js')

    @allure.step
    def attach_step_2(self):
        allure.attach('raw text', '附件 TEXT', extension='.txt')

    @allure.step
    def attach_step_3(self):
        allure.attach.file('test_demo_01/test_02.py', '附件 test_02.txt', extension='.txt')
