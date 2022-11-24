# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : MainWindow.py
@Project  : RToolBox
@Time     : 2022/11/23 17:32
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/23 17:32        1.0             None
"""
import sys

import clr

from Views.SearchWindow import SearchWindow
from Views.SettingWindow import SettingWindow
from Views.HelpWindow import HelpWindow
from Views.AboutWindow import AboutWindow
from Views.PluginWindow import PluginWindow
from Views.ViewBase import ViewBase
from Helpers.PluginManege.InstallPlugin import InstallPlugin
from Helpers.PluginManege.LoadPlugin import LoadPlugin
clr.AddReference(r"wpf\PresentationFramework")

from System.IO import *
from System.Windows.Markup import XamlReader
from System.Windows import *


class MainWindow(ViewBase):
    def __init__(self):
        """
        载入布局
        """
        try:
            stream = StreamReader(r'Views\MainWindow.xaml')
            self.window = XamlReader.Load(stream.BaseStream)
            """
            注册和绑定菜单事件 -- 开始
            """
            self.Install_item = LogicalTreeHelper.FindLogicalNode(self.window, "install_item")
            self.Install_item.Click += RoutedEventHandler(self.Install_Click)
            self.Exit_item = LogicalTreeHelper.FindLogicalNode(self.window, "exit_item")
            self.Exit_item.Click += RoutedEventHandler(self.Exit_Click)
            self.Search_item = LogicalTreeHelper.FindLogicalNode(self.window, "search_item")
            self.Search_item.Click += RoutedEventHandler(self.Search_Click)
            self.Setting_item = LogicalTreeHelper.FindLogicalNode(self.window, "setting_item")
            self.Setting_item.Click += RoutedEventHandler(self.Setting_Click)
            self.Plugin_item = LogicalTreeHelper.FindLogicalNode(self.window, "plugin_item")
            self.Plugin_item.Click += RoutedEventHandler(self.Plugin_Click)
            self.Help_item = LogicalTreeHelper.FindLogicalNode(self.window, "help_item")
            self.Help_item.Click += RoutedEventHandler(self.Help_Click)
            self.Doc_item = LogicalTreeHelper.FindLogicalNode(self.window, "doc_item")
            self.Doc_item.Click += RoutedEventHandler(self.Doc_Click)
            self.About_item = LogicalTreeHelper.FindLogicalNode(self.window, "about_item")
            self.About_item.Click += RoutedEventHandler(self.About_Click)
            """
            注册和绑定菜单事件 -- 结束
            """

            """
            加载插件
            """
            LoadPlugin()

            app = Application()
            app.Run(self.window)
        except Exception as ex:
            MessageBox.Show(ex)

    """
    菜单事件
    """

    @staticmethod
    def Install_Click(sender, e):
        InstallPlugin()

    @staticmethod
    def Exit_Click(sender, e):
        pass

    @staticmethod
    def Search_Click(sender, e):
        win = SearchWindow()

    @staticmethod
    def Setting_Click(sender, e):
        win = SettingWindow()

    @staticmethod
    def Plugin_Click(sender, e):
        win = PluginWindow()

    @staticmethod
    def Help_Click(sender, e):
        win = HelpWindow()

    @staticmethod
    def Doc_Click(sender, e):
        try:
            url = 'https://blog.900803.xyz/'
            import webbrowser
            webbrowser.open(url)
        except Exception as ex:
            MessageBox.Show(ex)

    @staticmethod
    def About_Click(sender, e):
        win = AboutWindow()
