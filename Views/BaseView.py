# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : BaseView.py
@Project  : jhq223
@Time     : 2022/12/7 13:31
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 13:31        1.0             None
"""

from gi.repository import Gtk
from ViewModels.BaseViewModel import BaseViewModel


class BaseView(Gtk.Window):
    def __init__(self, view_model: BaseViewModel):
        super().__init__()
        self.view_model = view_model
