#!/usr/bin/env python3.7

#imports 'os' , which enables Python to perform various file/folder operations and provides Operting System functionality 
import os

#imports 'global,' which is used to return file paths that match specific patterns
import glob

#defines the current working directory w/a 'cwd_path' variable
cwd_path = os.getcwd( )

#creates an empty 'list' named 'cwd_path_files'
cwd_path_files = [ ]

#uses a 'for' loop w/ a global 'glob' function to get ALL files and pathnames from the current working directory 'cwd'
for file in glob.glob(cwd_path + '/*'):
    
    #creates a 'dictionary' named 'cwd_path_size_dict' that stores file path(s) and size(s)
    cwd_path_size_dict = {"PATH": file, "SIZE": os.path.getsize(file)}
    
    #changes and adds the 'dictionary' to the cwd_path-file 'list'
    cwd_path_files.append(cwd_path_size_dict)
    
    #'range' function prints files to a more human-readable format
    for i in range(len(cwd_path_files)):
        print(cwd_path_files)
    
    
    
    



