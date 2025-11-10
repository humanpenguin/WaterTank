#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3
BorderButton.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing, copy, time
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
            self.handlers = {'event'     : None,
                             'flash'     : False,
                             'press_time': 0,
                             'short_help': " ",
                             'long_help' : """ """}
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
            self.bord_flash = (str(self.config.get("COLOURS","FlashBordB")),
                               str(self.config.get("COLOURS","ButtBorder")))
            return kwargs
        except Exception as e:
            print(f"An error occurred in BButton.build_self: {e}")

    def event_manager(self, s_help, l_help, *func: object):
        """

        :param l_help:
        :param *func:
        :type s_help: String
        """
        try:
            self.handlers['event'] = func
            self.handlers['flash'] = False
            self.handlers['press_time'] = time.time()
            self.handlers['short_help'] = s_help
            self.handlers['long_help'] = l_help
            self.button.bind("<ButtonPress>", self.but_press)
            self.button.bind("<ButtonRelease>", self.but_release)
        except Exception as e:
            print(f"An error occurred in BButton.event_manager: {e}")

    def flash_butt(self, index=0):
        try:
            if self.handlers['flash']:
                index = 1 - index
                self.configure(background=self.bord_flash[index])
                self.after(self.config.getint("BUTTON","FlaTime"),
                           lambda: self.flash_butt(1 - index) )
            else:
                self.configure(background=self.bord_flash[0])
        except Exception as e:
            print(f"An error occurred in BButton.flash_butt: {e}")

    def but_press(self):
        """ """
        try:
            self.handlers['press_time'] = time.time()
            self.handlers['flash'] = True
            self.flash_butt()
        except Exception as e:
            print(f"An error occurred in BButton.but_press: {e}")

    def but_release(self):
        """ """
        try:
            self.after(600, self.flash_off)
            pressed = time.time() - self.handlers['press_time']
            if pressed <= 500:
                lambda :self.handlers['event']
            elif pressed <= 2000:
                print(self.handlers["short_help"])
            else:
                print(self.handlers["long_help"])
        except Exception as e:
            print(f"An error occurred in BButton.but_release: {e}")

    def flash_off(self):
        """ """
        self.handlers['flash'] = False

