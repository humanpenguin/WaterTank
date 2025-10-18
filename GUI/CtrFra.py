#!/usr/bin/python3
"""
CtrFra.py: 
  Description 

"""
######################################################################
# Pypi Import
#
import typing, copy
import configparser as cf

######################################################################
# Local Import
#
import TopFrame as tf

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

class CtrFra(tf.TopFrame):
    """
    """
    def __init__(self, *args, **kwargs):
        Loc_kwargs = copy.copy(kwargs)
        super().__init__(*args, **Loc_kwargs)
        self.build_buts()
        
        
        
        
    