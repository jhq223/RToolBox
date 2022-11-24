# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : InstallPlugin.py
@Project  : RToolBox
@Time     : 2022/11/24 13:22
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/11/24 13:22        1.0             None
"""
import json
import os
import sys
import zipfile

import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.Windows import *
from Microsoft.Win32 import *


class InstallPlugin:
    def __init__(self):
        path = self.ChooseFile()
        if not path is None:
            self.Install(path)

    @staticmethod
    def Install(path):
        f = zipfile.ZipFile(path, 'r')
        data_txt = f.read("config.json")
        data = json.loads(data_txt)
        plugin_name = data["name"]
        install_path = os.path.join("Plugins", plugin_name)
        for file in f.namelist():
            f.extract(file, install_path)
        MessageBox.Show("插件安装成功!", "提示")

    @staticmethod
    def ChooseFile():
        openFileDialog = OpenFileDialog()
        openFileDialog.Filter = "插件包 (.zip)|*.zip|All files (*.*)|*.*"
        result = openFileDialog.ShowDialog()
        if result:
            return openFileDialog.FileName
        else:
            return None
