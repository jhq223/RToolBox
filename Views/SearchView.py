# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SearchView.py
@Project  : jhq223
@Time     : 2022/12/8 18:15
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 18:15        1.0             None
"""
from ViewModels import BaseViewModel
from Views.BaseView import BaseView
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SearchView(BaseView):
    def __init__(self, view_model: BaseViewModel):
        super(SearchView, self).__init__(view_model)
        self.view_model = view_model
        self.window = Gtk.Window(title="Hello World")
        self.window.set_position(Gtk.WindowPosition.CENTER)
        # 设置窗口大小
        self.window.set_default_size(800, 600)
        self.window.show()
