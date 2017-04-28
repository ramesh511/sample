#!/usr/bin/env python

import argparse
from ripdoss import Ripdoss

def read_dos(eval_path):
    """Interface with the Ripdoss class
    """
    
    cur_dos = Ripdoss(eval_path)
    cur_dos.print_info()

    

def main_function_call():

    samp_parser = argparse.ArgumentParser()

    samp_parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],dest="verbose_inp",
                        help="increase output verbosity")

    samp_parser.add_argument("-x", type=str,dest="xml",
                             help="path to XML file to process", required=True)
    samp_args = samp_parser.parse_args()

   # print "ARGUMENT {0}".format(samp_args)
	
    check_file = samp_args.xml
    
    if check_file:
        print "file {0}".format(check_file)

    read_dos(check_file)

        
if __name__ == "__main__":
    main_function_call()
