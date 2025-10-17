#!/usr/bin/python3
"""
TopFrame.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing
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
        self.config = kwargs.pop("config")
        super().__init__(*args, **kwargs)
        self.bg = self.config.get("COLOURS","Background")
        self.height = self.config.getint("ROOT","Height")
        self.width  = self.config.getint("ROOT","Width")
        
        
        
        
    