#Intermediate code used to parse the source code file given.

import os as oss
import subprocess as sp
import re as regex
import sys

global REGEX

#Fix on how to read filepaths
def read (file_path):

    return 0

def evaluate(filepath,language):
    
 if language == 'c':

  file = open (filepath, 'r')
  lines = file.readlines()
  file.close()
  vuln_count = 0
  vuln_count = vuln_count + gets_func_check(lines)
  vuln_count = vuln_count + format_string_check(lines)


 print( "Vulnerabilities found", countgets )


 return 0

#Possible function idea here.
def duplicatewc(fileVarName):
    return 0

#Fix this for it to work on any machine.
def fileread(filePath):
  #file = open(filePath, "r")
  sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
  stderr = sp.STDOUT
  print( stderr )

  #lines = file.readlines()
  #file.close()
  #fileshow(lines)
  return filePath

def fileshow(fileName):
    file = open( fileName, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        print ( line )
    return 0

def savefile(im, name):
    return 0

def gets_func_check(source_code):

  #look for patterns
  count = 0
  line_num = 0
  for line in lines:
    #This is where the vulnerabilities are checked.  
    #Separate the vulnerability checks as functions.
    REGEX = regex.search("gets[(].*[)]", line)
    line = line.strip()
    line_num = line_num + 1
    if REGEX:
       count = count + 1
       print(REGEX.span(), REGEX.lastindex)
       for m in regex.finditer("gets[(].*[)]", line):
           print("line :", line_num)
           print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    print("Buffer Overflow via gets() found: " + count)
    return count

def format_string_check(source_code):
    count = 0
    line_num = 0
    for line in source_code:
        REGEX = regex.search("printf[(].*[)]",line) 
        line = line.strip()
        linenumber = line_num +1
        if REGEX:
            count = count + 1
            print(REGEX.span(), REGEX.lastindex)
            for m in regex.finditer("printf[(].*[)]",line):
                print("line :", line_num)
                print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    print("Format String Vulnerabilities found: " + count)
    return count
