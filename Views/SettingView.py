# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SettingView.py
@Project  : jhq223
@Time     : 2022/12/10 14:01
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/10 14:01        1.0             None
"""
import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Views.BaseView import BaseView
from Helper.SettingHelper import SettingHelper


class SettingView(BaseView):
    def __init__(self, view_model):
        super(SettingView, self).__init__(view_model)
        self.setting_help = SettingHelper()
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "setting_window.glade")
        builder.add_from_file(path)
        # 获取窗口对象
        self.window = builder.get_object("setting_window")

        # 获取控件
        self.btn_theme = builder.get_object("btn_theme")
        self.btn_theme.set_popup(self.setting_help.theme_menu)
        self.btn_theme.set_label(self.setting_help.theme)
        self.btn_font = builder.get_object("btn_font")
        self.btn_font.set_label(self.setting_help.font)
        self.switch_night = builder.get_object("switch_night")
        self.btn_lang = builder.get_object("btn_lang")
        self.btn_lang.set_popup(self.setting_help.lang_menu)
        self.btn_lang.set_label(self.setting_help.lang)
        self.btn_ok = builder.get_object("btn_ok")
        self.btn_close = builder.get_object("btn_close")
        self.btn_apply = builder.get_object("btn_apply")

        # 绑定事件
        self.btn_ok.connect("clicked", self.view_model.btn_ok_click)
        self.btn_close.connect("clicked", self.view_model.btn_close_click)
        self.btn_apply.connect("clicked", self.view_model.btn_apply_click)
        self.btn_font.connect("font-set", self.view_model.btn_font_set)

        self.view_model.window = self.window

        self.window.set_title("设置")
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.show_all()
