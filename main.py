# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : main.py
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
from System.Threading import Thread, ThreadStart, ApartmentState
from Views.MainWindow import MainWindow

if __name__ == '__main__':
    thread = Thread(ThreadStart(MainWindow))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()
