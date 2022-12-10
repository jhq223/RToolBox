# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SearchViewModel.py
@Project  : jhq223
@Time     : 2022/12/8 18:16
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 18:16        1.0             None
"""
import importlib

from Helper.PluginHelper import PluginHelper
from ViewModels.BaseViewModel import BaseViewModel
import gi
import re

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class SearchViewModel(BaseViewModel):
    def __init__(self):
        super(SearchViewModel, self).__init__()
        self.plugin_help = PluginHelper()
        self.search_list = []
        self.search_list_store = Gtk.ListStore(str, str, str, str, bool, str)

    def search_click(self, weight):
        if self.in_search.get_text() == "":
            dialog = Gtk.MessageDialog(
                flags=0,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="提示",
            )
            dialog.format_secondary_text(
                "请输入搜索内容"
            )
            dialog.set_position(Gtk.WindowPosition.CENTER)
            dialog.run()
            dialog.destroy()
        else:
            self.load_list()

    def load_list(self):
        pattern = self.in_search.get_text()
        self.search_list.clear()
        for plugin in self.plugin_help.all_list:
            if re.match(pattern, plugin.name):
                self.search_list.append(plugin)
        self.search_list_store.clear()
        for plugin in self.search_list:
            self.search_list_store.append(PluginHelper.get_info(plugin))

    def search_treeview_click(self, weight, path, cow):
        index = eval(str(path))
        plugin = self.search_list[index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()
