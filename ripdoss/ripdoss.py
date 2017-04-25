### RIPDOSS module
import sys

if sys.hexversion < 0x020700F0:
  print >>sys.stderr, "Error: requires Python 2.7 or more recent."
  sys.exit()

import argparse
from xml.etree import cElementTree as ET


# define a class
class Ripdoss(object):
    """Class to Read IP DOS XML Datafile and report various values:

    Attributes:
        _file_path: A string representing the file path
        _xml_file:  ETree XML Object
        _xml_root:  ETree XML Root
    """

    def __init__(self, set_path):
        """Return a Ripdoss object whose name is *_file_path*.
        balance is *balance*."""

        self._file_path = set_path
        
        try:
            print "Reading File Path".format(self._file_path)
            
            self._xml_file = ET.parse(self._file_path)
            self._xml_root = self._xml_file.getroot()

        except IOError:
            print >>sys.stderr, "Unable to read [{0}]".format(self._file_path)
            self._xml_file = None
            

    def _getModule(self, mod_name):
        """_getModule method to find a module and return a pointer to it"""
        for io_module in self._xml_root.findall("io_module"):
            print "module {0}".format(io_module.findtext("name"))
            if io_module.findtext("name") == mod_name:
                return io_module
            return None


    def _getRegisterList(self, mod_pointer, reg_list=None):
        """_getRegister method to return a list of registers"""

        if reg_list is None:
            reg_list = []
        
        for register in mod_pointer.findall("registers/register"):
            reg_list.append(register)


    def print_info(self):
        """Print information about the IP DOS XML Datafile"""
        print "File Path [{0}]".format(self._file_path)

        ds_module = self._xml_root.find("io_module")
        mod_name = ds_module.findtext("name")
        print "Checking {0} from [{1}] XML...".format(mod_name, self._file_path)
        ic_module = self._getModule(mod_name)
        
        if not ic_module:
            print "** Module {0} not found in IC XML file".format(mod_name)

        check_reg_list = []
        self._getRegisterList(ic_module, check_reg_list)

        print "Registers..."
        
        for ds_register in check_reg_list:
            reg_name = ds_register.findtext("name")
            reg_offset = ds_register.findtext("addr_offset")
            reg_access = ds_register.findtext("access")
            reg_reset_val = ds_register.findtext("reset_value")
            print "reg [{0}] offset [{1}] access [{2}] reset [{3}]".format(reg_name, reg_offset, reg_access, reg_reset_val)
            
        
