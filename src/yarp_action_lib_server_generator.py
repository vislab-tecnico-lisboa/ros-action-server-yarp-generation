# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/plinio/.spyder2/.temp.py
"""
import subprocess

class yarp_action_lib_server_generator:

    def __init__(self,io_inputs):
        self.file_name = io_inputs['file_name']
        self.directory_name = io_inputs['dir_name']
        
    def generate_mgs_files(self):
        #call python script
        subprocess.call(['rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.directory_name], shell=True)
        print 'rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.directory_name
        #rosrun actionlib_msgs genaction.py Fibonacci.action -o ./msg