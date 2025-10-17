#!/usr/bin/python3
"""
BorderButton.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing
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

class BButton(Frame):
    """
    """
    def __init__(self, *args, **kwargs):
        self.config = kwargs.pop("config")
        super().__init__(*args, **kwargs)
        self.xpad