import clr

clr.AddReference(r"wpf\PresentationFramework")
from System.IO import *
from System.Windows.Markup import XamlReader, ParserContext
from System.Windows import *
from System.Windows.Controls import *
from Views.ViewBase import ViewBase


class Plugin1(ViewBase):
    def __init__(self):
        print("Success")
