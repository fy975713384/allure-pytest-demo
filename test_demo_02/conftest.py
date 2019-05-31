# -*- coding: utf-8 -*-
import allure
import pytest


@pytest.fixture
def initial():
    step_in_conftest()


@allure.step('step in test_demo_02/conftest.py')
def step_in_conftest():
    pass
