# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : ManageView.py
@Project  : jhq223
@Time     : 2022/12/10 19:12
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/10 19:12        1.0             None
"""

import os
import gi

from Helper.PluginHelper import PluginHelper

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Views.BaseView import BaseView


class ManageView(BaseView):
    def __init__(self, view_model):
        super(ManageView, self).__init__(view_model)
        self.view_model = view_model
        self.plugin_help = PluginHelper()
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "manage_window.glade")
        builder.add_from_file(path)
        # 获取窗口对象
        self.window = builder.get_object("manage_window")
        self.view_model.window = self.window

        # 加载全部插件
        self.all_list_store = Gtk.ListStore(str, str, str, str, bool, str)
        for plugin in self.plugin_help.all_list:
            self.all_list_store.append(PluginHelper.get_info(plugin))
        self.manage_treeview = builder.get_object("manage_treeview")
        self.load_title_layout(self.manage_treeview)
        self.manage_treeview.set_model(self.all_list_store)
        self.manage_treeview.connect("button_press_event", self.view_model.manage_treeview_click)
        self.window.set_title("插件管理")
        self.window.set_default_size(600, 500)
        self.window.show_all()



    @staticmethod
    def load_title_layout(weight, model: int = 0):
        tittle_list1 = ["名称", "版本", "备注", "描述", "收藏", "分类"]
        tittle_list2 = ["名称", "版本", "备注", "描述", "分类"]
        tittle_list3 = ["名称", "版本", "备注", "描述", "收藏"]
        if model == 0:
            use_t = tittle_list1
        elif model == 1:
            use_t = tittle_list2
        elif model == 2:
            use_t = tittle_list3
        for i, title in enumerate(use_t):
            col = Gtk.TreeViewColumn(title, Gtk.CellRendererText(), text=i)
            weight.append_column(col)
