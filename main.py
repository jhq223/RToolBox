import os

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from Views.MainView import MainView
from ViewModels.MainViewModel import MainViewModel


if __name__ == "__main__":
    settings = Gtk.Settings.get_default()
    settings.set_property("gtk-font-name", "Sans 12")
    settings.set_property("gtk-theme-name", "Windows-10-3.2.1")
    settings.set_property("gtk-application-prefer-dark-theme", False)
    image_path = os.path.join(os.path.abspath('.'), 'app.png')
    pix_buf = GdkPixbuf.Pixbuf.new_from_file(image_path)
    scaled_pix_buf = pix_buf.scale_simple(25, 25, GdkPixbuf.InterpType.HYPER)
    Gtk.Window.set_default_icon(scaled_pix_buf)
    MainView(MainViewModel())
    Gtk.main()
