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

from ViewModels.BaseViewModel import BaseViewModel
from ViewModels.SearchVIewModel import SearchViewModel
from Views.SearchView import SearchView
class MainViewModel(BaseViewModel):
    def __init__(self):
        super(MainViewModel, self).__init__()

    def m_new_select(self, weight):
        pass

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