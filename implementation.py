import os as oss
import subprocess as sp
import re as regex

matches ={}
class Match( object):
 def __init__(self, line, start, end, param):
         self.line = line
         self.start = start
         self.end = end
         self.param = param
def read (file_path):

    return 0

def evaluate(filepath,language):
 global x
 global newMatch
 global paraMatch
 global m1
 global lines
 global countgets

 global line_Strcpy
 global line_Print

 if language == 'c':

  file = open (filepath, 'r')
  lines = file.readlines()
  # str = file.read()
  file.close()


  #look for patterns
  countgets =0
  # countSTRNC =0
  linenumber =0

  for line in lines:
    x = regex.finditer("gets[(].*[)]", line)
    line = line.strip()
    linenumber = linenumber + 1
    if x:
       countgets = countgets + 1
       for m in regex.finditer("gets[(].*[)]", line):
           newMatch = Match(linenumber,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           newMatch.line = linenumber
           newMatch.start = m.start()
           newMatch.end = m.end()
           newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           print ("WARNING")
           print("at line: ", newMatch.line)
           print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

           # print("start at index: ", newMatch.start)
           # print(" ends at index: ", newMatch.end)
           # print(" param: ", newMatch.param)

  line_Strcpy = 0
  for line in lines:
    is_strcpy = regex.finditer("strcpy[(].*[)]", line)
    line = line.strip()
    line_Strcpy = line_Strcpy + 1

    if is_strcpy:

        for m in regex.finditer("strcpy[(].*[)]", line):
            newMatch = Match(line_Strcpy, m.start(), m.end(), line[(m.start() + 5): (m.end() - 1)])
            newMatch.line = line_Strcpy
            newMatch.start = m.start()
            newMatch.end = m.end()
            newMatch.param = line[(m.start() + 5): (m.end() - 1)]

            print("WARNING")
            print("at line: ", newMatch.line)
            print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

  line_Printf = 0
  for line in lines:
    is_Printf = regex.finditer("printf[(].*[)]", line)
    line = line.strip()
    line_Printf = line_Printf + 1

    if is_strcpy:

        for m in regex.finditer("printf[(].*[)]", line):
            newMatch = Match(line_Printf, m.start(), m.end(), line[(m.start() + 5): (m.end() - 1)])
            newMatch.line = line_Printf
            newMatch.start = m.start()
            newMatch.end = m.end()
            newMatch.param = line[(m.start() + 5): (m.end() - 1)]

            print("WARNING")
            print("at line: ", newMatch.line)
            print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

    # elif countgets> 0:
    #
    #
    #  for m in regex.finditer(newMatch.param, line):
    #
    #     paraMatch = Match(linenumber,m.start(),m.end(),"null")
    #     line = line.strip()
    #     paraMatch = Match(linenumber - 1, m.start(), m.end(), line[(m.start() + 5): (m.end() - 1)])
    #  if m:
    #     print("at line: ", paraMatch.line)
    #     # print("at start index: ", paraMatch.start)
    #     # print("at end index: ", paraMatch.end)
    #     linenumber = linenumber + 1


      # print("\n start at index: ", paraMatch.start)
      # print("\n ends at index: ", paraMatch.end)
      # print("\n param: ", paraMatch.param)
      # print( "vulnerabilities found", countgets )


  return 0

def duplicatewc(fileVarName):
    return 0


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