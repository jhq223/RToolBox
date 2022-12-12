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


class ManagePlugin(BaseModel):
    def __init__(self):
        super(ManagePlugin, self).__init__()
        self.dir_path = os.path.join(os.path.abspath('.'), "Plugins\\")

    def install_plugin_file(self, path) -> bool:
        """
               安装插件文件。

               :param path: 插件文件的路径。
               :return: 安装成功返回True，否则返回False。
        """
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
        """
                卸载插件文件。

                :param plugin: 要卸载的插件。
                :return: 卸载成功返回True，否则返回False。
        """
        try:
            plugin_path = os.path.join(self.dir_path, plugin.name)
            shutil.rmtree(plugin_path)
        except Exception as ex:
            print(ex)

    def create_plugin_files(self, plugin: Plugin) -> bool:
        """
         创建插件文件。

         :param plugin: 要创建的插件。
         :return: 创建成功返回True，否则返回False。
         """
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

    def change_json(self, info: list, plugin: Plugin):
        """
        将给定的信息写入config.json文件中，并将该文件存储在插件所对应的目录下。

        :param info: 一个包含所需信息的列表。
        :param plugin: 要创建的插件。
        :return: 创建成功返回True，否则返回False。
        """
        plugin_path = os.path.join(self.dir_path, plugin.name)
        config_path = os.path.join(plugin_path, "config.json")
        p_json = {"name": info[0],
                  "start": plugin.start,
                  "version": info[1],
                  "c_name": info[2],
                  "description": info[3],
                  "collected": str(info[4]),
                  "categorization": info[5]}
        with open(config_path, "w") as f:
            f.write(json.dumps(p_json))
