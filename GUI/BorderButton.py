#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3
BorderButton.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing, copy
import configparser as cf
from tkinter import Frame, Button

######################################################################
# Local Import
#

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

class BButton( Frame):
    """
    """
    def __init__(self, *args, **kwargs):
        #try:
            self.config = kwargs.pop("config")
            flpad = self.config.getint("BUTTON","Padd")
            bg_col= str(self.config.get("COLOURS","Background"))
            fg_col= str(self.config.get("COLOURS","Foreground"))
            bd_col= str(self.config.get("COLOURS","ButtBorder"))

            super().__init__(*args, **kwargs)
            self.configure( padx=flpad, pady=flpad, background=bd_col)
            self.button = Button(self, **kwargs)
            self.button.configure( background=bg_col)
            
        #except Exception as e:
        #    print(f"An error occurred: {e}")
