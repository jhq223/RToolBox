# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : MainView.py
@Project  : jhq223
@Time     : 2022/12/7 19:11
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 19:11        1.0             None
"""

# 引入必要的库
import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from Views.BaseView import BaseView
from Helper.PluginHelper import PluginHelper

class MainView(BaseView):
    def __init__(self, view_model):
        super(MainView, self).__init__(view_model)

        # 使用 glade 文件定义用户界面布局
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "main_window.glade")
        builder.add_from_file(path)

        self.plugin_help = PluginHelper()
        print(self.plugin_help.all_list)

        # 获取窗口对象
        self.window = builder.get_object("main_window")

        # 设置标题
        self.window.set_title("RToolBox")
        self.window.set_position(Gtk.WindowPosition.CENTER)
        # 设置窗口大小
        self.window.set_default_size(800, 600)

        # 获取菜单对象
        self.m_new = builder.get_object("m_new")
        self.m_install = builder.get_object("m_install")
        self.m_quit = builder.get_object("m_quit")
        self.m_search = builder.get_object("m_search")
        self.m_settings = builder.get_object("m_settings")
        self.m_manage = builder.get_object("m_manage")
        self.m_help = builder.get_object("m_help")
        self.m_about = builder.get_object("m_about")

        # 为按钮绑定单击事件处理方法
        self.m_new.connect("activate", self.view_model.m_new_select)
        self.m_install.connect("activate", self.view_model.m_install_select)
        self.m_quit.connect("activate", Gtk.main_quit)
        self.m_search.connect("activate", self.view_model.m_search_select)
        self.m_settings.connect("activate", self.view_model.m_settings_select)
        self.m_manage.connect("activate", self.view_model.m_manage_select)
        self.m_help.connect("activate", self.view_model.m_help_select)
        self.m_about.connect("activate", self.view_model.m_about_select)

        # Show the window
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
