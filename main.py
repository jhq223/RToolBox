import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Views.MainView import MainView
from ViewModels.MainViewModel import MainViewModel

if __name__ == "__main__":
    settings = Gtk.Settings.get_default()
    settings.set_property("gtk-theme-name", "Windows-10-3.2.1")
    settings.set_property("gtk-application-prefer-dark-theme", False)
    MainView(MainViewModel())
    Gtk.main()
