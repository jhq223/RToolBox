# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SettingViewModel.py
@Project  : jhq223
@Time     : 2022/12/10 14:02
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/10 14:02        1.0             None
"""
import shelve

from ViewModels.BaseViewModel import BaseViewModel
from Helper.SettingHelper import SettingHelper


class SettingViewModel(BaseViewModel):
    def __init__(self):
        super(SettingViewModel, self).__init__()
        self.setting_help = SettingHelper()

    def btn_ok_click(self, weight):
        self.setting_help.back()

    def btn_close_click(self, weight):
        self.setting_help.save()
        self.setting_help.back()
        self.window.destroy()

    def btn_apply_click(self, weight):
        self.setting_help.back()
        self.setting_help.loads()
        self.window.destroy()

    def btn_font_set(self, weight):
        self.setting_help.font = weight.get_font_name()
        weight.set_label(self.setting_help.font)
        with shelve.open("data") as db:
            db["font"] = self.setting_help.font
