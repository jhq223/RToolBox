# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : ManagePlugin.py
@Project  : jhq223
@Time     : 2022/12/8 23:36
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 23:36        1.0             None
"""
import json
import os
import shutil
import zipfile

from Models.BaseModel import BaseModel
from Models.Plugin import Plugin


class ManegePlugin(BaseModel):
    def __init__(self):
        super(ManegePlugin, self).__init__()
        self.dir_path = os.path.join(os.path.abspath('.'), "Plugins\\")

    def install_plugin_file(self, path) -> bool:
        try:
            f = zipfile.ZipFile(path, 'r')
            if "config.json" in f.namelist():
                json_txt = f.read("config.json")
                data = json.loads(json_txt)
                plugin_name = data["name"]
                install_path = os.path.join("Plugins", plugin_name)
                for file in f.namelist():
                    f.extract(file, install_path)
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def uninstall_plugin_file(self, plugin: Plugin) -> bool:
        try:
            plugin_path = os.path.join(self.dir_path, plugin.name)
            shutil.rmtree(plugin_path)
        except Exception as ex:
            print(ex)

    def create_plugin_files(self, plugin: Plugin) -> bool:
        plugin_path = os.path.join(self.dir_path, plugin.name)
        config_path = os.path.join(plugin_path, "config.json")
        py_path = os.path.join(plugin_path, f"{plugin.start}.py")
        p_json = {"name": plugin.name,
                  "start": plugin.start,
                  "version": plugin.version,
                  "c_name": plugin.c_name,
                  "description": plugin.description}
        if os.path.exists(plugin_path):
            return False
        else:
            try:
                os.makedirs(plugin_path)
                with open(config_path, "x") as f:
                    f.write(json.dumps(p_json))

                with open(py_path, "x") as f:
                    f.write(f"class {plugin.start}:\n\tdef __init__(self):\n\t\tprint(\"hello world!\")")

            except Exception as ex:
                print(ex)
            return True
