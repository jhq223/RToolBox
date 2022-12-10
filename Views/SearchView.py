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
import os

from ViewModels import SearchViewModel
from Views.BaseView import BaseView
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SearchView(BaseView):
    def __init__(self, view_model: SearchViewModel):
        super(SearchView, self).__init__(view_model)
        self.view_model = view_model
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "search_window.glade")
        builder.add_from_file(path)

        # 获取窗口对象
        self.window = builder.get_object("search_window")

        # 获取控件
        self.in_search = builder.get_object("in_search")
        self.btn_search = builder.get_object("btn_search")
        self.search_treeview = builder.get_object("search_treeview")

        # 传递控件
        self.view_model.in_search = self.in_search
        self.view_model.btn_search = self.btn_search
        self.view_model.search_treeview = self.search_treeview

        self.load_title_layout(self.search_treeview)
        self.search_treeview.set_model(self.view_model.search_list_store)

        # 绑定事件
        self.btn_search.connect("clicked", self.view_model.search_click)
        self.window.set_title("搜索")
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.search_treeview.connect("row-activated", self.view_model.search_treeview_click)

        # 设置窗口大小
        self.window.set_default_size(500, 400)
        self.window.show_all()

    @staticmethod
    def load_title_layout(weight):
        tittle_list1 = ["名称", "版本", "备注", "描述", "收藏", "分类"]
        for i, title in enumerate(tittle_list1):
            col = Gtk.TreeViewColumn(title, Gtk.CellRendererText(), text=i)
            weight.append_column(col)
