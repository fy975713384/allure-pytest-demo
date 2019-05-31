# -*- coding: utf-8 -*-
import allure


class Test03:
    """
    Allure Features - descriptions
    """

    # 案例一
    @allure.description("""
    Multiline test description.
    That comes from the allure.description decorator.
    
    Nothing special about it.
    """)
    def test_case_01(self):
        assert True

    # 案例二
    @allure.description_html("""
    <h1>Test with some complicated html description</h1>
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr align="center">
        <td>pan</td>
        <td>feng</td>
        <td>18</td>
      </tr>
    </table>
    """)
    def test_case_02(self):
        assert True

    # 案例三
    def test_case_03(self):
        """Unicode:
        你好

        Hello

        こんにちは

        여보세요

        שלום
        """
        assert True
