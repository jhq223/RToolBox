# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : Plugin.py
@Project  : jhq223
@Time     : 2022/12/8 10:05
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/8 10:05        1.0             None
"""

from Models.BaseModel import BaseModel


class Plugin(BaseModel):
    """
        Plugin 类用来描述一个插件的基本信息。

        继承自 BaseModel 类。
        """
    def __init__(self, name: str, start: str, version: str, c_name: str = None, description: str = None,
                 collected: bool = False, categorization: str = None):
        """
        初始化 Plugin 类。

        :param name: 插件的名称
        :param start: 插件的启动命令
        :param version: 插件的版本
        :param c_name: 插件的中文名，默认为 None
        :param description: 插件的描述，默认为 None
        :param collected: 插件是否被收藏，默认为 False
        :param categorization: 插件的所属分类，默认为 None
        """
        super(Plugin, self).__init__()
        self._name = name
        self._start = start
        self._version = version
        self._c_name = c_name
        self._description = description
        self._collected = collected
        self._categorization = categorization

    @property
    def name(self) -> str:
        return self._name

    @property
    def start(self) -> str:
        return self._start

    @property
    def version(self) -> str:
        return self._version

    @property
    def c_name(self) -> str:
        """
        获取插件中文名，注意，当为None时应该做判空处理
        """
        return self._c_name

    @c_name.setter
    def c_name(self, value: str) -> None:
        self._c_name = value

    @property
    def description(self) -> str:
        if self._description is not None:
            return self._description
        else:
            return "无描述"

    @property
    def collected(self) -> bool:
        return self._collected

    @collected.setter
    def collected(self, value: bool) -> None:
        self._collected = value

    @property
    def categorization(self) -> str:
        if self._categorization is not None:
            return self._categorization
        else:
            return "默认分类"

    @categorization.setter
    def categorization(self, value: str) -> None:
        self._categorization = value
