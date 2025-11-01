#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3

root.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import copy, typing
import configparser as cf
from tkinter import Tk, PhotoImage

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
        loc_kwargs = copy.deepcopy(kwargs)
        self.config = loc_kwargs.pop("config")
        super().__init__(*args, **loc_kwargs)
        icfp   = PhotoImage(self.config.get("PATHS","IconPath")+"/"+
                            self.config.get("ICONS","Window"))
        height = self.config.getint('ROOT','Height')
        width  = self.config.getint('ROOT','Width')
        xpos   = self.config.getint('ROOT','Xpos')
        ypos   = self.config.getint('ROOT','Ypos')
        self.geometry(str(width)+"x"+str(height)+
                      "+"+str(xpos)+"+"+str(ypos))
        self.title(self.config.get('ROOT','Tittle'))
        self.resizable(False, False)
        self.iconphoto(True, icfp)
        
        