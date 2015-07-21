# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:54:59 2015

@author: plinio
"""

from fileinput import *

def process_input(args):
    for line in fileinput.input(args):
        print line
    
if __name__ == "__main__":
   process_input(sys.argv[1:])
   #Run the following command to get the .msg files
   #rosrun actionlib_msgs genaction.py Fibonacci.action -o ./msg