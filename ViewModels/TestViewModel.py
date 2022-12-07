# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : TestViewModel.py
@Project  : jhq223
@Time     : 2022/12/7 16:52
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 16:52        1.0             None
"""

from ViewModels.BaseViewModel import BaseViewModel


class TestViewModel(BaseViewModel):

    def __init__(self):
        super(TestViewModel, self).__init__()
        self.text = ""

    def on_button_click(self, weight: object) -> None:
        weight.set_label(self.text)

    def on_change(self, weight) -> None:
        self.text = weight.get_text()