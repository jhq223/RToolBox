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

import clr

clr.AddReference(r"wpf\PresentationFramework")

from System.IO import *
from System.Windows.Markup import XamlReader
from System.Windows import *
from Views.ViewBase import ViewBase
from Views.AboutWindow import AboutWindow

class MainWindow(ViewBase):
    def __init__(self):
        try:
            stream = StreamReader(r'Views\MainWindow.xaml')
            self.window = XamlReader.Load(stream.BaseStream)
            self.Button1 = LogicalTreeHelper.FindLogicalNode(self.window, "button1")
            self.Button1.Click += RoutedEventHandler(self.Button_Click)
            app = Application()
            app.Run(self.window)
        except Exception as ex:
            print(ex)

    def Button_Click(self, sender, e):
        print('clicked')
        # MessageBox.Show(self.Button1.Content + " is clicked!")
        win = AboutWindow()
