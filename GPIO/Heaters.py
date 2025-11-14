#!/home/dave/Software/Development/WaterTank/bin/python3
"""
/usr/bin/python3
Heaters.py:
  Description 

"""
######################################################################
# Pypi Import
#


######################################################################
# Local Import
#
######################################################################
# Pypi Import
import typing, copy

__author__    = "David A Hall "
__copyright__ = """Copyright 2025, David A Hall
                   HumanPenguin@GMail.com
                   Licence GPL 3.0 see LICENCE.md
"""

class Heaters():
    """
    """
    def __init__(self, *args, **kwargs):
        self.args = copy.deepcopy(kwargs)
        self.config = self.args.pop("config")
        # init Set Power Source On
        self.MainsOn = self.BattsOn = self.SolDAct = self.MoorAct = False
        self.MainsTime = self.BattsTime = False

    def Mains_Switch(self):
        self.MainsOn = not self.MainsOn

    def Batts_Switch(self):
        self.BattsOn = not self.BattsOn

    def SolDu_Switch(self):
        self.SolDAct = not self.SolDAct

    def MoorA_Switch(self):
        self.MoorAct = not self.MoorAct