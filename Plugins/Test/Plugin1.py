import os

import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.IO import *
from System.Windows.Markup import XamlReader, ParserContext
from System.Windows import *
from System.Windows.Controls import *
from Views.ViewBase import ViewBase


class Plugin1(ViewBase):
    def __init__(self):
        try:
            dirpath = os.path.split(os.path.realpath(__file__))[0]
            path = os.path.join(dirpath, "Plugin1.xaml")
            stream = StreamReader(path)
            self.window = XamlReader.Load(stream.BaseStream)
            self.window.Show()
        except Exception as ex:
            MessageBox.Show(ex)
