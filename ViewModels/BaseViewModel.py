# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : BaseViewModel.py
@Project  : jhq223
@Time     : 2022/12/7 13:31
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/7 13:31        1.0             None
"""
import gi
from gi.repository import GObject
from Models.BaseModel import BaseModel


class BaseViewModel(GObject.Object):
    def __init__(self, model: BaseModel = None):
        super(BaseViewModel, self).__init__()
