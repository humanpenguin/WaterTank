#!/usr/bin/python3
"""
CtrFra.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing, copy, pprint
import configparser as cf
import tkinter as tk

######################################################################
# Local Import
#
import GUI.TopFrame as tf
import GUI.BorderButton as bb

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

class CtrFra(tf.TopFrame):
    """
    """
    def __init__( self, *args, **kwargs):
        self.args = kwargs
        self.config = copy.deepcopy(kwargs['config'])
        
        super().__init__(*args, **kwargs)
        self.build_buts()
        self.build_layout()
        
        
    def build_buts( self):
        cl_icon = tk.PhotoImage(self.config.get('ICONS','Close'))
        pprint.pprint(self.args)
        self.Close_Butt = bb.BButton(self, config=self.config, image=cl_icon, command=self.close())
    
    def build_layout( self):
        self.Close_Butt.grid(column=5,row=5)
        
        
    def close( self):
        self.winfo_toplevel().destroy()
        
        
    