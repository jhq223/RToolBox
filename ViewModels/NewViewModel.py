# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : NewViewModel.py
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

from ViewModels.BaseViewModel import BaseViewModel
from Helper.ManagePlugin import ManagePlugin
from Models.Plugin import Plugin
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NewViewModel(BaseViewModel):
    def __init__(self):
        super(NewViewModel, self).__init__()
        self.manage_plugin = ManagePlugin()

    def create_click(self, weight):
        name = self.in_name.get_text()
        start = self.in_start.get_text()
        version = self.in_version.get_text()
        if name == "" or start == "" or version == "":
            dialog = Gtk.MessageDialog(
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text="错误",
            )
            dialog.format_secondary_text(
                "请将插件必填信息填写完整"
            )
            dialog.set_position(Gtk.WindowPosition.CENTER)
            dialog.run()
            dialog.destroy()
        else:
            if self.in_des.get_text() == "":
                des = None
            else:
                des = self.in_des.get_text()
            plugin = Plugin(name=self.in_name.get_text(), start=self.in_start.get_text(),
                            version=self.in_version.get_text(), c_name=self.in_c_name.get_text(),
                            description=des)
            if not self.manage_plugin.create_plugin_files(plugin):
                dialog = Gtk.MessageDialog(
                    flags=0,
                    message_type=Gtk.MessageType.ERROR,
                    buttons=Gtk.ButtonsType.OK,
                    text="错误",
                )
                dialog.format_secondary_text(
                    "创建失败，可能是插件目录存在同名插件"
                )
                dialog.set_position(Gtk.WindowPosition.CENTER)
                dialog.run()
                dialog.destroy()

            else:
                dialog = Gtk.MessageDialog(
                    flags=0,
                    message_type=Gtk.MessageType.INFO,
                    buttons=Gtk.ButtonsType.OK,
                    text="提示",
                )
                dialog.format_secondary_text(
                    "插件创建成功"
                )
                dialog.set_position(Gtk.WindowPosition.CENTER)
                dialog.run()
                dialog.destroy()
