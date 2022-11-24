# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : ViewBase.py
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
from System.Windows import *


class ViewBase(Window):

    def __init__(self):
        super(ViewBase, self).__init__(self)



