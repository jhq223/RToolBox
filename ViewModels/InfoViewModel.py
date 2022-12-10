# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : InfoViewModel.py
@Project  : jhq223
@Time     : 2022/12/10 21:18
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/10 21:18        1.0             None
"""
from Helper.ManagePlugin import ManagePlugin
from ViewModels.BaseViewModel import BaseViewModel
from Helper.PluginHelper import PluginHelper


class InfoViewModel(BaseViewModel):
    def __init__(self, plugin):
        super(InfoViewModel, self).__init__()
        self.plugin = plugin
        self.plugin_help = PluginHelper()
        self.info = self.plugin_help.get_info(self.plugin)
        self.manage_help = ManagePlugin()

    def btn_ok_click(self, weight):
        self.info[0] = self.name.get_text()
        self.info[1] = self.version.get_text()
        self.info[2] = self.c_name.get_text()
        self.info[3] = self.des.get_text()
        self.info[4] = self.col.get_active()
        self.info[5] = self.cat.get_text()
        self.manage_help.change_json(self.info, self.plugin)
        self.window.destroy()

    def btn_close_click(self, weight):
        self.window.destroy()
