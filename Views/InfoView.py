# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : InfoView.py
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

import os
import gi

from Helper.PluginHelper import PluginHelper
from Models.Plugin import Plugin
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject
from Views.BaseView import BaseView


class InfoView(BaseView):
    def __init__(self, view_model):
        super(InfoView, self).__init__(view_model)
        self.view_model = view_model
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "info_window.glade")
        builder.add_from_file(path)
        # 获取窗口对象
        self.window = builder.get_object("info_window")
        self.view_model.window = self.window
        print(self.view_model.info)
        self.name = builder.get_object("name")
        self.name.set_text(self.view_model.info[0])
        self.name.set_editable(False)
        self.version = builder.get_object("version")
        self.version.set_text(self.view_model.info[1])
        self.version.set_editable(False)
        self.c_name = builder.get_object("c_name")
        if self.view_model.info[2] is None:
            self.c_name.set_text("")
        else:
            self.c_name.set_text(self.view_model.info[2])

        self.des = builder.get_object("des")
        self.des.set_text(self.view_model.info[3])
        self.col = builder.get_object("col")
        self.col.set_active(self.view_model.info[4])
        self.cat = builder.get_object("cat")
        self.cat.set_text(self.view_model.info[5])
        self.btn_ok = builder.get_object("btn_ok")
        self.btn_close = builder.get_object("btn_close")

        self.btn_ok.connect("clicked", self.view_model.btn_ok_click)
        self.btn_close.connect("clicked", self.view_model.btn_close_click)

        self.view_model.name = self.name
        self.view_model.version = self.version
        self.view_model.c_name = self.c_name
        self.view_model.des = self.des
        self.view_model.col = self.col
        self.view_model.cat = self.cat

        self.window.set_title("插件信息")
        self.window.set_default_size(500, 400)
        self.window.show_all()
