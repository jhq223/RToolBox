import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Views.MainView import MainView
from Helper.SettingHelper import SettingHelper
from ViewModels.MainViewModel import MainViewModel


if __name__ == "__main__":
    SettingHelper()
    MainView(MainViewModel())
    Gtk.main()
