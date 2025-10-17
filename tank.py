#!/usr/bin/python3
"""
tank.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import configparser
from tkinter import Tk, font

######################################################################
# Local Import
#
import GUI.root as rt
import GUI.TopFrame as tf

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

def main( **args):
    config = configparser.ConfigParser()
    config.read("/home/dave/Software/Development/WaterTank/Data/config.ini")
    
    root      = rt.RootWindow(config=config)
    top_frame = tf.TopFrame(root, config=config)
    top_frame.pack()
    root.mainloop()
    
    

if __name__ == "__main__":
    main()
