#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3
BorderButton.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing, copy, time, subprocess
import configparser as cf
from tkinter import Frame, Button, font as tkFont, PhotoImage, GROOVE, RAISED

######################################################################
# Local Import
#

__author__ = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""


class BButton(Frame):
    """
    """
    bord_flash: tuple[str, str]

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        try:
            self.parent = args[0]
            kwargs = self.build_self(**kwargs)
            super().__init__(*args, **kwargs)
            self.buttondict["highlightcolor"] = str(self.config.get("COLOURS", "HiBackgrou"))
            self.buttondict["highlightthickness"] = 1
            self.framedict["background"] = str(self.config.get("COLOURS", "ButtBorder"))
            self.configure(self.framedict)
            self.button = Button(self, **kwargs)
            self.button.configure(self.buttondict)
            self.button.pack()
        except Exception as e:
            print(f"An error occurred in BButton.__init__: {e}")

    def build_self(self, **kwargs):
        """

        :type kwargs: object
        """
        try:
            self.framedict = dict()
            self.buttondict = dict()
            keys = kwargs.copy()
            for key in keys.keys():
                if key == "config":
                    self.config = kwargs.pop("config")
                elif key == "image":
                    imagenm = kwargs.pop("image")
                    imagest = "./Icons/" + str(self.config.get('ICONS', imagenm))
                    self.image = PhotoImage(file=imagest)
                    self.buttondict["image"] = self.image
                elif key == "text":
                    self.buttondict["text"] = kwargs.pop("text")
            self.framedict["padx"] = self.framedict["pady"] = self.config.getint("BUTTON", "Padd")
            self.buttondict["background"] = str(self.config.get("COLOURS", "Background"))
            self.buttondict["activebackground"] = str(self.config.get("COLOURS", "Background"))
            self.buttondict["relief"] = RAISED
            self.buttondict["overrelief"] = RAISED
            self.buttondict["foreground"] = str(self.config.get("COLOURS", "Foreground"))
            self.buttondict["activeforeground"] = str(self.config.get("COLOURS", "Foreground"))
            font = tkFont.Font(family=str(self.config.get("BUTTON", "FontFam")),
                               size=str(self.config.get("BUTTON", "FontSiz")),
                               weight=tkFont.BOLD)
            self.buttondict["font"] = font
            self.buttondict["background"] = str(self.config.get("COLOURS", "Background"))
            self.buttondict["foreground"] = str(self.config.get("COLOURS", "Foreground"))
            self.buttondict["highlightbackground"] = str(self.config.get("COLOURS", "Background"))
            self.bord_flash = (str(self.config.get("COLOURS","ButtBorder")),
                               str(self.config.get("COLOURS","FlashBordB")))
            return kwargs
        except Exception as e:
            print(f"An error occurred in BButton.build_self: {e}")

    def event_manager(self, s_help, l_help, func: object):
        """

        :param l_help:
        :param func:
        :type s_help: String
        """
        try:
            self.handler = self.Hand(s_help, l_help, func)
            self.handler.flash = False
            self.button.bind("<ButtonPress>", self.but_press)
            self.button.bind("<ButtonRelease>", self.but_release)
        except Exception as e:
            print(f"An error occurred in BButton.event_manager: {e}")

    def flash_butt(self, index=False):
        try:
            if self.handler.flash:
                if index: flacol = self.bord_flash[1]
                else: flacol = self.bord_flash[0]
                self.configure(background=flacol)
                self.after(self.config.getint("BUTTON","FlaTime"),
                           lambda: self.flash_butt(not index))
            else:
                self.configure(background=self.bord_flash[0])
        except Exception as e:
            print(f"An error occurred in BButton.flash_butt: {e}")

    def but_press(self, e):
        """ """
        try:
            self.handler.set_time()
            self.handler.switch_flash()
            self.flash_butt()
        except Exception as e:
            print(f"An error occurred in BButton.but_press: {e}")

    def but_release(self, e):
        """ """
        try:
            self.after(600, self.handler.switch_flash())
            pressed = time.time() - self.handler.press_time
            if pressed <= (self.config.getint("BUTTON","ShortPress")/1000):
                self.handler.event()
            elif pressed <= (self.config.getint("BUTTON","LongPress")/1000):
                self.espeak(self.handler.short_help)
            else:
                self.espeak(self.handler.long_help)
        except Exception as e:
            print(f"An error occurred in BButton.but_release: {e}")

    def espeak(self, text: str) :
        """ Use espeak to convert text to speech. """
        subprocess.run(['espeak','-k20','-p40', '-m' ,'<break> '+text])

    class Hand():
        event: object

        def __init__(self, s_help = "", l_help = """""", func = None):
            self.event      = func
            self.flash      = False
            self.press_time = 0
            self.short_help = s_help
            self.long_help  = l_help

        def switch_flash(self):
            self.flash = not self.flash

        def set_time(self):
            self.press_time = time.time()