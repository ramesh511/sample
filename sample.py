#!/usr/bin/env python

import argparse
from ripdoss import Ripdoss

def read_dos(eval_path):
    """Interface with the Ripdoss class
    """
    
    cur_dos = Ripdoss(eval_path)
    cur_dos.print_info()

    

def main():

    samp_parser = argparse.ArgumentParser()

    samp_parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")

    samp_parser.add_argument("-x", "--xml", type=str,
                             help="path to XML file to process", required=True)
   
    samp_args = samp_parser.parse_args()

    check_file = samp_args.xml
    
    if check_file:
        print "file {0}".format(check_file)

    read_dos(check_file)

        
if __name__ == "__main__":
    main()
