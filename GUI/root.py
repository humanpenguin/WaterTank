#!/usr/bin/python3
"""
root.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing
import configparser as cf
from tkinter import Tk

######################################################################
# Local Import
#

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
		
"""

class RootWindow(Tk):
    """
    """
    def __init__(self, *args, **kwargs):
        self.config = kwargs.pop("config")
        super().__init__(*args, **kwargs)
        self.height = self.config.getint('ROOT','Height')
        self.width  = self.config.getint('ROOT','Width')
        
        
        
        
    