# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/plinio/.spyder2/.temp.py
"""
import subprocess
import os
import sys

class yarp_action_lib_server_generator:

    def __init__(self,io_inputs):
        self.file_name = io_inputs['file_name']
        self.action_directory_name = io_inputs['action_dir_name']
        self.relative_action_dir_name = io_inputs['rel_action_dir_name']
        self.code_directory_name = io_inputs['code_dir_name']
        self.relative_code_dir_name = io_inputs['rel_code_dir_name']
#        self.absolute_path = io_inputs['path']
        
    def generate_mgs_files(self):
        #call python script
        subprocess.call(['rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.action_directory_name], shell=True)
        print 'rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.action_directory_name
        #rosrun actionlib_msgs genaction.py Fibonacci.action -o ./msg
    
    def generate_buffered_port_files(self):
        #For all the files in the folder
        for root, dirs, files in os.walk(self.action_directory_name):
            for name in files:
                print name, root
                origWD = os.getcwd() # remember our original working directory
                os.chdir(os.path.join(os.path.abspath(sys.path[0]), self.relative_action_dir_name))
                subprocess.Popen(['yarpidl_rosmsg','--out ' , self.code_directory_name + '/include ' ,  name]) 
                os.chdir(origWD) # get 
                #subprocess.call(['yarpidl_rosmsg --out ' + self.code_directory_name + '/include ' + ' ./' + self.relative_action_dir_name + '/' + name], shell=True)
                #print ['yarpidl_rosmsg --out ' + './' + self.code_directory_name + '/include ' + ' ./' + self.relative_action_dir_name + '/' + name]