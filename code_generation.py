# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:54:59 2015

@author: plinio
"""

from fileinput import *
import argparse
from ConfigParser import RawConfigParser
from src.yarp_action_lib_server_generator import yarp_action_lib_server_generator as action_gen

def process_input():
#    for line in fileinput.input(args):
#        print line
    parser = argparse.ArgumentParser()
    parser.add_argument('-if','--input', type = argparse.FileType('r'), help='Text file that contains the action file (-af) and the directory (-ad)')
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument('-af','--action_file', help='ROS-formatted action file')
    parser.add_argument('-ad','--action_dir', help='Directory where .msg files will be stored')
    args = parser.parse_args()
    if args.input:
        if args.verbose:
            print "Reading input file {}".format(args.input.name)
        config = RawConfigParser()
        config.readfp(args.input)
        action_file_str = config.get('main','action_file')
        action_dir_str = config.get('main', 'action_dir')
        if args.verbose:
            print 'Action file: ' + action_file_str
            print 'Directory to store the msg files: ' + action_dir_str
#    elif args.input and (not args.verbose):
#        config = RawConfigParser()
#        config.readfp(args.input)
#        action_file_str = config.get('main','action_file')
#        action_dir_str = config.get('main', 'action_dir')
    elif args.action_file and args.action_dir:
        action_file_str = args.action_file
        action_dir_str = args.action_dir
        if args.verbose:
            print 'Action file: ' + action_file_str
            print 'Directory to store the msg files: ' + action_dir_str
    else:
        print 'Missing arguments for proper execution'
        parser.print_help()
        action_file_str='';
        action_dir_str=''
    try:
        absolute_path_fn = os.path.dirname(__file__) + '/actions/' + action_file_str
        absolute_dir_name = os.path.dirname(__file__) + '/' + action_dir_str
        print absolute_path_fn
        print absolute_dir_name
        my_temp_fp = open(absolute_path_fn)
        my_temp_fp.close()
    except IOError:
        print 'Action file does not exist'
    return {'file_name': absolute_path_fn, 'dir_name': absolute_dir_name}
#        for line in args.input:
#            print line,
if __name__ == "__main__":
   absolute_io_inputs = process_input()
   action_code_generator = action_gen(absolute_io_inputs)
   action_code_generator.generate_mgs_files()
   #Run the following command to get the .msg files
   #rosrun actionlib_msgs genaction.py Fibonacci.action -o ./msg