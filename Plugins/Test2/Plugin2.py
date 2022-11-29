import os
import requests
import json
import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.IO import *
from System.Windows.Markup import XamlReader, ParserContext
from System.Windows import *
from System.Windows.Controls import *
from Views.ViewBase import ViewBase


class Plugin2(ViewBase):
    def __init__(self):
        try:
            dirpath = os.path.split(os.path.realpath(__file__))[0]
            path = os.path.join(dirpath, "Plugin2.xaml")
            stream = StreamReader(path)
            self.window = XamlReader.Load(stream.BaseStream)
            """
            注册和绑定事件
            """

            self.Text1 = LogicalTreeHelper.FindLogicalNode(self.window, "text1")
            self.Text2 = LogicalTreeHelper.FindLogicalNode(self.window, "text2")
            self.Button1 = LogicalTreeHelper.FindLogicalNode(self.window, "button1")
            self.Button1.Click += RoutedEventHandler(self.Button1_Click)

            self.window.Show()
        except Exception as ex:
            MessageBox.Show(ex)

    def Button1_Click(self, sender, e):
        url = "http://fanyi.youdao.com/translate?&doctype=json&type=EN2ZH_CN&i="
        text1 = self.Text1.Text
        r = requests.get(str(url + text1))
        datajson = json.loads(r.content)
        data = datajson["translateResult"][0][0]
        self.Text2.Text = data["tgt"]

