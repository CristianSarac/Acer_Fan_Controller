#!/usr/bin/python


from gi.repository import Gtk,Notify
import subprocess
import os


class FanAcer(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("FanAcer.glade")
        self.builder.connect_signals(self)
         # lets initialise with the application name
        Notify.init("FanAcer")
        window = self.builder.get_object("mainWindow")
        window.set_title("Acer Fan Controller")

    def run(self):
        self.builder.get_object("mainWindow").show_all()

        Gtk.main()

    def FanMaximum_clicked_cb(self, FanMaximum):
        # Open a subprocces to execute the perl script
        pipe = subprocess.Popen(['/usr/bin/pkexec', "perl",os.getcwd()+"/acer_5750G_fan_controller.pl", "MAX"],
                                stdout=subprocess.PIPE)

        stdoutdata, stderrdata = pipe.communicate()

        if (pipe.returncode==0):
            # Send a notification on the speed of the Fans
            n = Notify.Notification.new("FanAcer","Fan Speed set to Maximum")
            n.set_timeout(Notify.EXPIRES_NEVER)
            n.show()

    def FanNormal_clicked_cb(self, FanNormal):
         # Open a subprocces to execute the perl script
        pipe = subprocess.Popen(
            ['/usr/bin/pkexec', "perl",os.getcwd()+ "/acer_5750G_fan_controller.pl", "NORMAL"],
            stdout=subprocess.PIPE)

        stdoutdata, stderrdata = pipe.communicate()

        if (pipe.returncode==0):
            # Send a notification on the speed of the Fans
            n = Notify.Notification.new("FanAcer","Fan Speed set to Normal")
            n.set_timeout(Notify.EXPIRES_NEVER)
            n.show()



    def close_window(self, *args):
        Gtk.main_quit()


FanAcer().run()
