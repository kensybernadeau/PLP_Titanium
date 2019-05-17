import subprocess as sp
import re as regex
import platform

class Match( object):
    def __init__(self, line, start, end, param):
        self.line = line
        self.start = start
        self.end = end
        self.param = param

def read (file_path):
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

        print("Total potential vulnerabilities detected: " + str(count))
        return 0

def evaluate_overflow(filepath, language):
    if language == 'c':
        file = open(filepath,'r')
        source = file.readlines()
        file.close()

        count = 0

        count = count + gets_check(source)
        count = count + strcpy_check(source)

        print("Total potential overflows detected: " + str(count))
        return 0



#Cross-platforming idea here
def fileread(filePath):
    os_name = platform.system()
    if(os_name in 'Linux'):
        sp.call(['/bin/nano', filePath])
    elif(os_name in 'Windows'):
        sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
    elif(os_name in 'Darwin'):
        sp.call(['/usr/bin/nano', filePath])
    #sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
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
    print("RUNNING: gets() check")
    line_gets = 0
    count_gets = 0
    for line in source_code:
        is_gets = regex.finditer("gets[(].*[)]", line)
        line = line.strip()
        line_gets = line_gets + 1
        if is_gets:
            for m in regex.finditer("gets[(].*[)]", line):
                newMatch = Match(line_gets,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
                newMatch.line = line_gets
                newMatch.start = m.start()
                newMatch.end = m.end()
                newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

                # print("line :", linenumber)
                print ("WARNING")
                print("at line: ", newMatch.line)
                print('index(start- end) %02d-%02d: %s\n' % (m.start(), m.end(), m.group(0)))
                count_gets = count_gets + 1
    if count_gets > 0:
        print("SUGGESTION")
        print("Use fgets insetad of gets, since the use of gets has been deprecated due to overflow vulnerabilities.\n")
    else:
        print("No gets() has been found.\n")
    return count_gets




def printf_check(source_code):
    #Check for any printf()
    print("RUNNING: printf check")
    line_printf = 0
    count_printf = 0
    for line in source_code:
        is_printf = regex.finditer("printf[(].*[)]", line)
        line = line.strip()
        line_printf = line_printf + 1
        if is_printf:
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
                count_printf = count_printf +1
    if count_printf > 0:
        print("SUGGESTION:")
        print("Make sure printf is not taking in any user input.")
        print("In the case of user input use, make sure the input has been sanitized and the compiler has ASLR enabled.\n")
    else:
        print("No vulnerable printf functions has been found.\n")
    return count_printf

def strcpy_check(source_code):
    #Check for any strcpy()
    print("RUNNING: strcpy check")
    line_strcpy = 0
    count_strcpy = 0
    for line in source_code:
        is_strcpy = regex.finditer("strcpy[(].*[)]", line)
        line = line.strip()
        line_strcpy = line_strcpy + 1
        if is_strcpy:
            for m in regex.finditer("strcpy[(].*[)]", line):
                newMatch = Match(line_strcpy,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
                newMatch.line = line_strcpy
                newMatch.start = m.start()
                newMatch.end = m.end()
                newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

                # print("line :", linenumber)
                print ("WARNING")
                print("at line: ", newMatch.line)
                print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
                count_strcpy = count_strcpy + 1
    if count_strcpy > 0:
        print("SUGGESTION:")
        print("Use the str-n-func family of functions. The additional n is a parameter for maximum number of characters.\n")
    else:
        print("No strcpy functions found.\n")
    return count_strcpy


