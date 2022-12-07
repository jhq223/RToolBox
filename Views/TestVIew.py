# 引入必要的库
import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from Views.BaseView import BaseView


class TestView(BaseView):
    def __init__(self, view_model):
        super(TestView, self).__init__(view_model)

        # 使用 glade 文件定义用户界面布局
        builder = Gtk.Builder()
        dirpath = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.join(dirpath, "Testb.glade")
        builder.add_from_file(path)

        # 获取窗口对象
        self.window = builder.get_object("test_b")

        # Set the window title
        self.window.set_title("Test")

        # Set the window size
        self.window.set_default_size(800, 600)

        # 获取按钮对象
        self.btn_1 = builder.get_object("button1")

        self.label1 = builder.get_object("label1")
        self.input1 = builder.get_object("input1")

        binding = GObject.Binding.bind_property(
            self.input1, "text",
            self.label1, "label",
            GObject.BindingFlags.BIDIRECTIONAL,
        )

        # binding.connect("notify",self.view_model.on_change)

        # 为按钮绑定单击事件处理方法
        self.btn_1.connect("clicked", self.view_model.on_button_click)

        self.input1.connect("changed", self.view_model.on_change)

        # Show the window
        self.window.show_all()

        self.window.connect("destroy", Gtk.main_quit)
