#!/usr/bin/python


from gi.repository import Gtk
import subprocess
import os


class FanAcer(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("FanAcer.glade")
        self.builder.connect_signals(self)

    def run(self):
        self.builder.get_object("mainWindow").show_all()

        Gtk.main()

    def FanMaximum_clicked_cb(self, FanMaximum):

        pipe = subprocess.Popen(['/usr/bin/pkexec', "perl",os.getcwd()+"/acer_5750G_fan_controller.pl", "MAX"],
                                stdout=subprocess.PIPE)


    def FanNormal_clicked_cb(self, FanNormal):

        pipe = subprocess.Popen(
            ['/usr/bin/pkexec', "perl",os.getcwd()+ "/acer_5750G_fan_controller.pl", "NORMAL"],
            stdout=subprocess.PIPE)

    def close_window(self, *args):
        Gtk.main_quit()


FanAcer().run()
