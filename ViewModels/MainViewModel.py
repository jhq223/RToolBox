# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : MainViewModel.py
@Project  : jhq223
@Time     : 2022/12/7 19:13
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 19:13        1.0             None
"""
import importlib
import os

from ViewModels.BaseViewModel import BaseViewModel
from ViewModels.ManageViewModel import ManageViewModel
from ViewModels.SearchViewModel import SearchViewModel
from Views.ManageView import ManageView
from Views.SearchView import SearchView
from Views.NewView import NewView
from ViewModels.NewViewModel import NewViewModel
from Helper.ManagePlugin import ManagePlugin
from Views.SettingView import SettingView
from ViewModels.SettingViewModel import SettingViewModel
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class MainViewModel(BaseViewModel):
    def __init__(self):
        super(MainViewModel, self).__init__()
        self.manage_plugin = ManagePlugin()

    def m_new_select(self, weight):
        view_model = NewViewModel()
        NewView(view_model)

    def m_install_select(self, weight):
        dialog = Gtk.FileChooserDialog(
            title="请选择插件包", action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        dialog.set_position(Gtk.WindowPosition.CENTER)
        file_filter = Gtk.FileFilter()
        file_filter.set_name("Zip files")
        file_filter.add_pattern("*.zip")
        dialog.add_filter(file_filter)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            install_a = self.manage_plugin.install_plugin_file(dialog.get_filename())
            if install_a:
                dialog_i = Gtk.MessageDialog(
                    flags=0,
                    message_type=Gtk.MessageType.INFO,
                    buttons=Gtk.ButtonsType.OK,
                    text="提示",
                )
                dialog_i.format_secondary_text(
                    "插件安装成功"
                )
                dialog_i.set_position(Gtk.WindowPosition.CENTER)
                dialog_i.run()
                dialog_i.destroy()
            else:
                dialog_e = Gtk.MessageDialog(
                    flags=0,
                    message_type=Gtk.MessageType.ERROR,
                    buttons=Gtk.ButtonsType.OK,
                    text="安装失败",
                )
                dialog_e.format_secondary_text(
                    "插件包损坏或者不是插件包"
                )
                dialog_e.set_position(Gtk.WindowPosition.CENTER)
                dialog_e.run()
                dialog_e.destroy()

        dialog.destroy()

    def m_search_select(self, weight):
        search_model = SearchViewModel()
        SearchView(search_model)

    def m_settings_select(self, weight):
        setting_model = SettingViewModel()
        SettingView(setting_model)

    def m_manage_select(self, weight):
        manage_view_model = ManageViewModel()
        ManageView(manage_view_model)

    def m_help_select(self, weight):
        help_txt = """
1. 目录
    1.1 介绍
    1.2 安装说明
    1.3 基本操作
    1.4 常见问题
    1.5 反馈与建议

2. 介绍
    2.1 什么是RToolBox软件
    2.2 RToolBox软件的特点

3. 安装说明
    3.1 下载安装包
    3.2 安装步骤

4. 基本操作
    4.1 打开RToolBox软件
    4.2 新建工程
    4.3 编辑工程
    4.4 保存工程

5. 常见问题
    5.1 安装失败
    5.2 打开软件失败
    5.3 编辑工程时出错

6. 反馈与建议
    6.1 如何反馈问题
    6.2 如何提出建议
        """

        dialog_help = Gtk.Dialog()
        dialog_help.set_title("帮助")
        dialog_help.set_position(Gtk.WindowPosition.CENTER)
        dialog_help.set_default_size(600, 500)
        text_view = Gtk.TextView()
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(text_view)
        text_view.set_editable(False)
        text_view.set_cursor_visible(False)
        text_view.set_vexpand(True)
        text_buffer = text_view.get_buffer()
        text_buffer.insert(text_buffer.get_start_iter(), help_txt)
        dialog_help.get_content_area().add(scrolled_window)
        dialog_help.show_all()
        dialog_help.run()
        dialog_help.destroy()

    def m_about_select(self, weight):
        image_path = os.path.join(os.path.abspath('.'), 'app.png')
        pix_buf = GdkPixbuf.Pixbuf.new_from_file(image_path)
        scaled_pix_buf = pix_buf.scale_simple(100, 100, GdkPixbuf.InterpType.HYPER)
        about_dialog = Gtk.AboutDialog()
        about_dialog.set_program_name("RToolBox")
        about_dialog.set_version("1.0.0")
        about_dialog.set_copyright('Copyright (c) 2022 今何求')
        about_dialog.set_license_type(Gtk.License.MIT_X11)
        about_dialog.set_comments('一个Python工具箱')
        about_dialog.set_authors(['今何求'])
        about_dialog.set_website('https://blog.900803.xyz/')
        about_dialog.set_logo(scaled_pix_buf)
        about_dialog.set_position(Gtk.WindowPosition.CENTER)
        about_dialog.run()
        about_dialog.destroy()

    def all_treeview_click(self, weight, path, cow):
        index = eval(str(path))
        plugin = self.plugin_help.all_list[index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()

    def col_treeview_click(self, weight, path, cow):
        index = eval(str(path))
        plugin = self.plugin_help.collected[index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()

    def cat_treeview_clicked(self, weight, path, column):
        index = eval(str(path))
        key = weight.get_name()

        plugin = self.plugin_help.categories[key][index]
        module_name = f"Plugins.{plugin.name}.{plugin.start}"
        # 动态导入模块
        module = importlib.import_module(module_name)
        # 获取模块中的类
        Plugin = getattr(module, f"{plugin.start}")
        # 使用 Plugin1 类
        Plugin()
