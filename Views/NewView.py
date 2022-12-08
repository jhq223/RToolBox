# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : NewView.py
@Project  : jhq223
@Time     : 2022/12/8 22:28
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 22:28        1.0             None
"""
import os

from ViewModels import BaseViewModel
from Views.BaseView import BaseView
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NewView(BaseView):
    def __init__(self, view_model: BaseViewModel):
        super(NewView, self).__init__(view_model)
        self.view_model = view_model
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "new_window.glade")
        builder.add_from_file(path)
        # 获取窗口对象
        self.window = builder.get_object("new_window")

        # 获取控件
        self.in_name = builder.get_object("in_name")
        self.in_start = builder.get_object("in_start")
        self.in_version = builder.get_object("in_version")
        self.in_c_name = builder.get_object("in_c_name")
        self.in_des = builder.get_object("in_des")
        self.btn_create = builder.get_object("btn_create")

        # 传递控件
        self.view_model.in_name = self.in_name
        self.view_model.in_start = self.in_start
        self.view_model.in_version = self.in_version
        self.view_model.in_c_name = self.in_c_name
        self.view_model.in_des = self.in_des

        # 绑定事件
        self.btn_create.connect("clicked", self.view_model.create_click)
        self.window.set_title("创建插件")
        self.window.show_all()
