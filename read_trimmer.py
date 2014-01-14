#!/usr/bin/env python
# encoding: utf-8

"""
read_trimmer.py
Created by Emily Ebel on 1/14/13.

The author may be contacted at ebel@bu.edu.

This script takes a fastq file as input, trims the designated number
of characters from the front and end of the line of each sequence and
corresponding quality score, and returns the trimmed file.


# Licensing:

[ Note that for publication you have to make your code 
open source. There are a couple of open source licenses 
to choose from and http://choosealicense.com/ has a 
really nice break down of the standard options.]
"""

import argparse
import sys


def get_args():
    """Parse sys.argv"""
    
    #INITIATE PARSER
    parser = argparse.ArgumentParser()
    
    #ADD COMMANDLINE ARGUMENT
    parser.add_argument('-S', '--start',
                        required=True,
                        type=int,
                        help='Trim X number of bases from the start of each read.')
    parser.add_argument('-E', '--end',
                        required=True,
                        type=int,
                        help='Trim X number of bases from the start of each read.')
    parser.add_argument('INPUT',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs='?',
                        help='Input =fastq file.')
    parser.add_argument('OUTPUT',
                        type=argparse.FileType('r'),
                        default=sys.stdout,
                        nargs='?',
                        help='Output trimmed fastq file.')
    #PROCESS ARGUMENTS 
    args = parser.parse_args()
    return args




def worker_fuction_1():
    """Doc string...."""
    pass

def work_fuction_2():
    """Doc string...."""
    pass

# etc...

def main(args):
    """Main function.

    This code should be concise - typically a single loop that
    calls worker_fuctions that do most of the computation."""

    #access the args with, e.g, args.INPUT
    for line in enumerate(args.INPUT):
        count, txt = line
        if count % 4 == 1 or count % 4 == 3: #if it's a line of sequence or quality scores
            txt = txt.strip()
            txt = txt[args.start:] #trim the front
            txt = txt[:(-args.end-1)] #trim the back
            txt = txt+'\n'
            args.OUTPUT.write(txt)
        else:
            args.OUTPUT.write(txt)

            

if __name__ == '__main__':
    
    """This statement allows you have code in your program
    that is only executed if it is run as a command-line script.

    Explanation here:
    http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    It should only call in the args and the main function.
    """

    #call in the args
    args = get_args()
    
    #call main function    
    main(args)

