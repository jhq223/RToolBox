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

    def __init__(self):
        global plugins_list
        plugins_list = dict()
        self.Load()

    def Load(self):
        for filedir in os.listdir("Plugins"):
            path = os.path.join("Plugins", filedir)
            if not os.path.isdir(path):
                continue
            self.Get(path)

    @staticmethod
    def Get(path):
        with open(os.path.join(path, "config.json"), 'r', encoding='utf-8') as f:
            config_txt = f.read()
        data = json.loads(config_txt)
        sys.path.append(path)
        module = __import__(data["data"][1], fromlist=[data["data"][0], ])
        pluginClass = getattr(module, data["data"][1])
        pluginClass()

    def Run(self, pluginInfo):
        pass
