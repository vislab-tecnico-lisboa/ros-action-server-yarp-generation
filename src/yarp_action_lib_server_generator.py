# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/plinio/.spyder2/.temp.py
"""
import subprocess
import os
import sys
import re
class yarp_action_lib_server_generator:

    def __init__(self,io_inputs):
        self.file_name = io_inputs['file_name']
        self.action_directory_name = io_inputs['action_dir_name']
        self.relative_action_dir_name = io_inputs['rel_action_dir_name']
        self.code_directory_name = io_inputs['code_dir_name']
        self.relative_code_dir_name = io_inputs['rel_code_dir_name']
        self.action_server_cpp_file_name = io_inputs['rel_code_dir_name']
        self.action_name_str = re.sub('.action$', '', io_inputs['relative_action_file_name'])

#        self.absolute_path = io_inputs['path']
        
    def generate_mgs_files(self):
        #call python script
        #new_env = os.environ.copy()
        #subprocess.call(['rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.action_directory_name], shell=True, executable='/bin/bash')
        subprocess.call(['/bin/bash', '-i', '-c', 'rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.action_directory_name])
        print 'rosrun actionlib_msgs genaction.py ' + self.file_name + ' -o ' + self.action_directory_name
        #rosrun actionlib_msgs genaction.py Fibonacci.action -o ./msg
    
    def generate_buffered_port_files(self):
        #For all the files in the folder
        include_dir_str = self.code_directory_name + '/include'
        if not os.path.exists(include_dir_str):
            os.makedirs(include_dir_str)
        for root, dirs, files in os.walk(self.action_directory_name):
            for name in files:
                print name, root
                origWD = os.getcwd() # remember our original working directory
                os.chdir(os.path.join(os.path.abspath(sys.path[0]), self.relative_action_dir_name))
                #subprocess.Popen(['yarpidl_rosmsg','--out ' , self.code_directory_name + '/include ' ,  name]) 
                subprocess.Popen(['/bin/bash', '-i', '-c', 'yarpidl_rosmsg --out ' + self.code_directory_name + '/include ' +  name])
                os.chdir(origWD) # get
        os.chdir(os.path.join(os.path.abspath(sys.path[0]), self.relative_action_dir_name))
        #subprocess.Popen(['yarpidl_rosmsg','--out ' , self.code_directory_name + '/include ' ,  'actionlib_msgs/GoalStatusArray'])
        subprocess.Popen(['/bin/bash', '-i', '-c','yarpidl_rosmsg --out ' + self.code_directory_name + '/include + actionlib_msgs/GoalStatusArray'])
        os.chdir(origWD)
                #subprocess.call(['yarpidl_rosmsg --out ' + self.code_directory_name + '/include ' + ' ./' + self.relative_action_dir_name + '/' + name], shell=True)
                #print ['yarpidl_rosmsg --out ' + './' + self.code_directory_name + '/include ' + ' ./' + self.relative_action_dir_name + '/' + name]
    def generate_action_server_cpp(self):
        cpp_file_p = open(self.relative_code_dir_name + '/' + self.relative_code_dir_name + '_server.cpp', 'w')
        #Create two buffered ports for reading (goal and cancel)
        cpp_file_p.write('#include "' + self.action_name_str + 'ActionFeedback.h"\n')
        cpp_file_p.write('#include "' + self.action_name_str + 'ActionGoal.h"\n')
        cpp_file_p.write('#include "' + self.action_name_str + 'ActionResult.h"\n')
        cpp_file_p.write('#include "actionlib_msgs_GoalStatusArray.h"\n')
        cpp_file_p.write('#include "actionlib_msgs_GoalID.h"\n')
        cpp_file_p.close()
        #Create three buffered ports for writing (feedback, status and result)