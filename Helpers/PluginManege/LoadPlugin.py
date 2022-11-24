# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : LoadPlugin.py
@Project  : RToolBox
@Time     : 2022/11/24 13:21
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/24 13:21        1.0             None
"""
import json
import os
import sys


class LoadPlugin:
    plugins_list = []

    def __init__(self):

        self.Load()

    def Load(self):
        for filedir in os.listdir("Plugins"):
            path = os.path.join("Plugins", filedir)
            if not os.path.isdir(path):
                continue
            self.Get(path)

    def Get(self, path):
        with open(os.path.join(path, "config.json"), 'r', encoding='utf-8') as f:
            config_txt = f.read()
        # data = json.loads(config_txt)
        sys.path.append(path)
        self.plugins_list.append(config_txt)
