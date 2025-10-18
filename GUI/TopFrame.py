#!/usr/bin/python3
"""
TopFrame.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import copy 
import configparser as cf
from tkinter import Frame

######################################################################
# Local Import
#

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

class TopFrame(Frame):
    """
    """
    def __init__(self, *args, **kwargs):
        self.args = copy.deepcopy(kwargs)
        self.config = self.args.pop("config")
        super().__init__(*args, **self.args)
        self.bg = self.config.get("COLOURS","Background")
        self.height = self.config.getint("ROOT","Height")
        self.width  = self.config.getint("ROOT","Width")
        self.configure(background=self.bg, height=self.height, width=self.width)
        
        
    def getroot(self) -> object:
        try:
            root = self
            while self.master:
                root = self.master
            return root
        except Exception as e:
            print(f"An error occurred: {e}")