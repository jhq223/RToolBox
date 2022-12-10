# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : SettingHelper.py
@Project  : jhq223
@Time     : 2022/12/10 14:01
@Author   : 今何求
@Contact_1: jhq223@gmail.com
@Software : PyCharm
@License  : (C)Copyright 2022, 今何求
@Last Modify Time      @Version     @Desciption
--------------------       --------        -----------
2022/12/10 14:01        1.0             None
"""
import os
from Models.BaseModel import BaseModel
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import shelve
import os


class SettingHelper(BaseModel):
    def __init__(self):
        super(SettingHelper, self).__init__()
        self.settings = Gtk.Settings.get_default()
        image_path = os.path.join(os.path.abspath('.'), 'app.png')
        pix_buf = GdkPixbuf.Pixbuf.new_from_file(image_path)
        scaled_pix_buf = pix_buf.scale_simple(25, 25, GdkPixbuf.InterpType.HYPER)
        Gtk.Window.set_default_icon(scaled_pix_buf)
        self.theme_menu = Gtk.Menu()
        self.theme_menu.append(Gtk.MenuItem("Win"))
        self.theme_menu.append(Gtk.MenuItem("Adwaita"))
        self.theme_menu.append(Gtk.MenuItem("HighContrast"))
        self.theme_menu.show_all()
        self.theme_menu.connect("selection-done", self.theme_menu_selected)
        self.lang_menu = Gtk.Menu()
        self.lang_menu.append(Gtk.MenuItem("简体中文"))
        self.lang_menu.append(Gtk.MenuItem("English"))
        self.lang_menu.show_all()
        self.lang_menu.connect("selection-done", self.lang_menu_selected)
        if os.path.exists(os.path.join(os.path.abspath("."), "data.dat")):
            with shelve.open("data") as db:
                self._theme = db["theme"]
                self._font = " ".join(str(db["font"]).split(","))
                self._lang = db["lang"]
        else:
            with shelve.open("data") as db:
                db["theme"] = "Win"
                db["font"] = "Microsoft,JhengHei,Bold,12"
                db["lang"] = "简体中文"
                self._theme = db["theme"]
                self._font = " ".join(str(db["font"]).split(","))
                self._lang = db["lang"]

        self.loads()

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, theme):
        self._theme = theme
        self.save()

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        self._font = font
        self.save()

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        self._lang = lang
        self.save()

    def save(self):
        with shelve.open("data") as db:
            db["theme"] = self.theme
            db["font"] = " ".join(str(db["font"]).split(","))
            db["lang"] = self.lang

    def load_theme(self, theme: str):
        if theme == "Win":
            self.settings.set_property("gtk-theme-name", "Windows-10-3.2.1")
        elif theme == "HighContrast":
            self.settings.set_property("gtk-theme-name", "HighContrast")
        else:
            self.settings.set_property("gtk-theme-name", "Adwaita")

    def load_font(self, font: str):
        self.settings.set_property("gtk-font-name", font)

    def load_lang(self, lang):
        pass

    def theme_menu_selected(self, weight):
        self.theme = weight.get_active().get_label()
        weight.get_attach_widget().set_label(self.theme)
        self.save()

    def lang_menu_selected(self, weight):
        self.lang = weight.get_active().get_label()
        weight.get_attach_widget().set_label(self.lang)

    def loads(self):
        self.load_theme(self.theme)
        self.load_font(self.font)
        self.load_lang(self.lang)

    def back(self):
        with shelve.open("data") as db:
            self.theme = db["theme"]
            self.font = " ".join(str(db["font"]).split(","))
            self.lang = db["lang"]

