# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : MainViewModel.py
@Project  : jhq223
@Time     : 2022/12/7 19:13
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 19:13        1.0             None
"""
import importlib

from ViewModels.BaseViewModel import BaseViewModel
from ViewModels.SearchVIewModel import SearchViewModel
from Views.SearchView import SearchView
from Views.NewView import NewView
from ViewModels.NewViewModel import NewViewModel


class MainViewModel(BaseViewModel):
    def __init__(self):
        super(MainViewModel, self).__init__()

    def m_new_select(self, weight):
        view_model = NewViewModel()
        NewView(view_model)

    def m_install_select(self, weight):
        pass

    def m_search_select(self, weight):
        search_model = SearchViewModel()
        search_window = SearchView(search_model)

    def m_settings_select(self, weight):
        pass

    def m_manage_select(self, weight):
        pass

    def m_help_select(self, weight):
        pass

    def m_about_select(self, weight):
        print("about")

    def all_treeview_click(self, weight, path, cow):
        index = eval(str(path))
        plugin = self.plugin_help.all_list[index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()

    def col_treeview_click(self, weight, path, cow):
        index = eval(str(path))
        plugin = self.plugin_help.collected[index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()

    def cat_treeview_clicked(self, weight, path, column):
        index = eval(str(path))
        key = weight.get_name()

        plugin = self.plugin_help.categories[key][index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()
