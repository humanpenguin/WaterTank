#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3
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
        self.Close_Butt = bb.BButton(self, config=self.config, image="Close")
        self.Main_Butt = bb.BButton(self, config=self.config, width=5, text="Mains")
        self.Batt_Butt = bb.BButton(self, config=self.config, width=5, text="Batts")
        self.SolD_Butt = bb.BButton(self, config=self.config, width=5, text="Solar")
        self.Moor_Butt = bb.BButton(self, config=self.config, width=5, text="Moor")
    
    def build_layout( self):
        self.Close_Butt.place(x=680, y=360)
        self.Main_Butt.place(x=1, y=0)
        self.Batt_Butt.place(x=1, y=120)
        self.SolD_Butt.place(x=1, y=240)
        self.Moor_Butt.place(x=1, y=360)

    

    def close( self):
        self.winfo_toplevel().destroy()
        
        
    