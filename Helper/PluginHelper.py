# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : PluginHelper.py
@Project  : jhq223
@Time     : 2022/12/8 10:52
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 10:52        1.0             None
"""
import json
import os
from Models.BaseModel import BaseModel
from Models.Plugin import Plugin


def load_from_json(config_path) -> Plugin:
    # 读取 config.json 文件的内容
    with open(config_path, "r") as config_file:
        config_content = config_file.read()
    # 将 config.json 文件的内容解析为 Python 对象
    config = json.loads(config_content)
    name = config.get("name")
    start = config.get("start")
    version = config.get("version")
    c_name = config.get("c_name")
    description = config.get("description")
    collected = config.get("collected")
    if collected is None:
        collected = False
    categorization = config.get("categorization")
    plugin = Plugin(name, start, version, c_name, description, collected, categorization)
    return plugin


class PluginHelper(BaseModel):
    """
    PluginHelper 类用于管理插件的信息。
    """

    def __init__(self):
        """
        始化 PluginHelper 类。
        在初始化时，会自动加载插件的信息。
        """
        super(PluginHelper, self).__init__()
        self._all_list = []
        self._categories = {}
        self._collected = []
        self.load_all()
        self.load_categories()
        self.load_collect()

    @property
    def all_list(self):
        return self._all_list

    @property
    def categories(self):
        return self._categories

    @property
    def collected(self):
        return self._collected

    def load_all(self):
        plugins_folder = "Plugins"
        file_names = os.listdir(plugins_folder)
        for file_name in file_names:
            if os.path.isdir(os.path.join(plugins_folder, file_name)):
                config_path = os.path.join(plugins_folder, file_name, "config.json")
                if os.path.exists(config_path):
                    self.add_plugin(load_from_json(config_path))

    def load_categories(self):
        for plugin in self._all_list:
            self.add_category(plugin)

    def load_collect(self):
        for plugin in self._all_list:
            if plugin.collected:
                self._collected.append(plugin)

    def add_plugin(self, plugin: Plugin):
        self._all_list.append(plugin)

    def add_category(self, plugin: Plugin):
        category = plugin.categorization
        # 如果字典中不存在该分类，则添加一个新的键值对
        if category not in self._categories:
            self._categories[category] = []
            self._categories[category].append(plugin)
        else:
            self._categories[category].append(plugin)

    @staticmethod
    def get_info(plugin: Plugin, model: int = 0) -> list:
        if model == 0:
            info_list = [plugin.name, plugin.version, plugin.c_name,
                         plugin.description, plugin.collected, plugin.categorization]
        elif model == 1:
            info_list = [plugin.name, plugin.version, plugin.c_name,
                         plugin.description, plugin.categorization]
        elif model == 2:
            info_list = [plugin.name, plugin.version, plugin.c_name,
                         plugin.description, plugin.collected]
        return info_list
