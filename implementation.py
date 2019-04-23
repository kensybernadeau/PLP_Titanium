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
    x = regex.search("gets[(].*[)]", line)
    line = line.strip()
    linenumber = linenumber + 1
    if x:
       countgets = countgets + 1
      # print(x.span(), x.lastindex)
       for m in regex.finditer("gets[(].*[)]", line):
           newMatch = Match(linenumber,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           # newMatch.line = linenumber
           # newMatch.start = m.start()
           # newMatch.end = m.end()
           # newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           # print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
           # print( "at line: ", newMatch.line)
           # print("\n start at index: ", newMatch.start)
           # print("\n ends at index: ", newMatch.end)
           # print("\n param: ", newMatch.param)

    elif countgets> 0:


     for m in regex.finditer(newMatch.param, line):

        paraMatch = Match(linenumber,m.start(),m.end(),"null")
        line = line.strip()
        paraMatch = Match(linenumber - 1, m.start(), m.end(), line[(m.start() + 5): (m.end() - 1)])
     if m:
        print("at line: ", paraMatch.line)
        # print("at start index: ", paraMatch.start)
        # print("at end index: ", paraMatch.end)
        linenumber = linenumber + 1


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