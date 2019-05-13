import subprocess as sp
import re as regex


global newMatch

# Create a match class
class Match( object):
 def __init__(self, line, start, end, param):
         self.line = line
         self.start = start
         self.end = end
         self.param = param


def read (file_path):
    return 0

def duplicatewc(file_path):
    return 0

def savefile(file_path):
    return 0

def evaluate(filepath,language):


#Open the .c source code
 if language == 'c':
  file = open (filepath, 'r')
  source = file.readlines()
  # str = file.read()
  file.close()

  #Keep a count on how many vulnerabilities are found in the source code.
  count = 0

  count = count + gets_check(source)
  count = count + printf_check(source)
  count = count + strcpy_check(source)

  if(count == 0):
      print("There are no vulnerabilities in your code!! :) ")
  else:
        print("There are "+str(count)+" potential vulnerabilities in the code")


  return 0


#Cross-platforming idea here
def fileread(filePath):
  #file = open(filePath, "r")
  sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
  stderr = sp.STDOUT
  print( stderr )
  return filePath

def fileshow(fileName):
    file = open( fileName, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        print ( line )
    return 0

def gets_check(source_code):
  #Check for any gets()
  line_gets = 0
  count_gets = 0
  for line in source_code:
    is_gets = regex.finditer("gets[(].*[)]", line)
    line = line.strip()
    line_gets = line_gets + 1
    if is_gets:
       count_gets = count_gets + 1
       for m in regex.finditer("gets[(].*[)]", line):
           newMatch = Match(line_gets,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           newMatch.line = line_gets
           newMatch.start = m.start()
           newMatch.end = m.end()
           newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           print ("WARNING")
           print("at line: ", newMatch.line)
           print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    print("gets functions found: "+str(count_gets))
    return count_gets

def printf_check(source_code):
  #Check for any printf()
  line_printf = 0
  count_printf = 0
  for line in source_code:
    is_printf = regex.finditer("printf[(].*[)]", line)
    line = line.strip()
    line_printf = line_printf + 1
    if is_printf:
       count_printf = count_printf + 1
       for m in regex.finditer("printf[(].*[)]", line):
           newMatch = Match(line_printf,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           newMatch.line = line_printf
           newMatch.start = m.start()
           newMatch.end = m.end()
           newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           print ("WARNING")
           print("at line: ", newMatch.line)
           print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

    print("printf(parameter) functions found: "+str(count_printf))
    return count_printf

def strcpy_check(source_code):
  #Check for any strcpy()
  line_strcpy = 0
  count_strcpy = 0
  for line in source_code:
    is_strcpy = regex.finditer("strcpy[(].*[)]", line)
    line = line.strip()
    line_strcpy = line_strcpy + 1
    if is_strcpy:
       count_strcpy = count_strcpy + 1
       for m in regex.finditer("strcpy[(].*[)]", line):
           newMatch = Match(line_strcpy, m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           newMatch.line = line_strcpy
           newMatch.start = m.start()
           newMatch.end = m.end()
           newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           print ("WARNING")
           print("at line: ", newMatch.line)
           print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

    print("strcpy(parameter) functions found: "+str(count_strcpy))
    return count_strcpy
