#!/home/dave/Software/Development/bin/python3
"""
/usr/bin/python3
tank.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import configparser
import tkinter as tk
from tkinter import Tk, font

######################################################################
# Local Import
#
import GUI.root as rt
import GUI.CtrFra as cf

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

def main( **args):
    fp = open("/home/dave/Software/Development/WaterTank/Data/config.ini",'r')
    config = configparser.ConfigParser()
    config.read_file(fp)
    
    root      = rt.RootWindow(config=config)
    ctr_frame = cf.CtrFra(root, config=config)
    ctr_frame.place(x=0,y=0)
    root.mainloop()
    
if __name__ == "__main__":
    main()

