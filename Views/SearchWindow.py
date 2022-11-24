# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SearchWindow.py.py
@Project  : RToolBox
@Time     : 2022/11/24 10:51
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/24 10:51        1.0             None
"""

import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.IO import *
from System.Windows.Markup import XamlReader, ParserContext
from System.Windows import *
from System.Windows.Controls import *
from Views.ViewBase import ViewBase


class SearchWindow(ViewBase):
    def __init__(self):
        try:
            stream = StreamReader(r'Views/SearchWindow.xaml')
            self.window = XamlReader.Load(stream.BaseStream)
            self.window.Show()
        except Exception as ex:
            MessageBox.Show(ex)
