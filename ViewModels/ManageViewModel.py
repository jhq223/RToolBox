# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : ManageViewModel.py
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

from ViewModels.BaseViewModel import BaseViewModel
from Helper.ManagePlugin import ManagePlugin
from Helper.PluginHelper import PluginHelper
from Models.Plugin import Plugin
from Views.InfoView import InfoView
from ViewModels.InfoViewModel import InfoViewModel
import gi

from Views.BaseView import BaseView

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ManageViewModel(BaseViewModel):
    def __init__(self):
        super(ManageViewModel, self).__init__()
        self.plugin_help = PluginHelper()
        self.manage_help = ManagePlugin()
        self.p_path = 0
        self.menu = Gtk.Menu()
        # 创建菜单项
        menu_item1 = Gtk.MenuItem("修改")
        menu_item2 = Gtk.MenuItem("删除")

        self.menu.connect("selection-done", self.menu_click)

        # 将菜单项添加到菜单中
        self.menu.append(menu_item1)
        self.menu.append(menu_item2)

    def manage_treeview_click(self, weight, event):
        if event.button == 3:  # 如果是鼠标右键
            # 获取当前点击的行和列的信息
            x, y = event.get_coords()
            path_info = weight.get_path_at_pos(int(x), int(y))
            if path_info is not None:
                path, col, cell_x, cell_y = path_info
                self.p_path = int(str(path))
                # 显示菜单
                self.menu.show_all()
                self.menu.popup(None, None, None, None, button=event.button, activate_time=event.time)

    def menu_click(self, weight):
        key = weight.get_active().get_label()
        if key == "修改":
            info_view_model = InfoViewModel(self.plugin_help.all_list[self.p_path])
            InfoView(info_view_model)
        else:
            dialog = Gtk.MessageDialog(
                transient_for=self.window,
                flags=0,
                message_type=Gtk.MessageType.QUESTION,
                buttons=Gtk.ButtonsType.YES_NO,
                text="确认删除",
            )
            dialog.format_secondary_text(
                "确定要删除吗？"
            )
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                self.manage_help.uninstall_plugin_file(self.plugin_help.all_list[self.p_path])
            elif response == Gtk.ResponseType.NO:
                pass
            dialog.destroy()
