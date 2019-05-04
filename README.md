### **PLP_Titanium**
---
The PLP_Titanium System is a flexible framework for checking the vulnerabilities of C programming 
language and then providing suggestions of modification. This system has a collection of method that aim 
to find the potential risk of C language across various operating system, such as Windows, Linus, MacOS.   

### **Background Information**
---
For the novice in C program, there would be some potential risks that may damage the system. 
Especially, if the system is a online platform, these risks may lead to severe securities issues.
PLP_Titanium, therefore, provides a very accessible way to reminds these novice user of the existence of 
such risk. 

### **Language Features**
---
There are three features about this language. First, it will detect the potential risks. Second it will 
display the location(the No. of line) where the risks occur. At last, the language can provide the 
suggestions that may secure the program.  

### **Sample Codes**
---
#### Example 1: Get() method checker
```
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
```
#### Example 2: Strcpy() method checker
```
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
           newMatch = Match(line_Gets,m.start(),m.end(),line[(m.start() + 5 ): (m.end()- 1)])
           newMatch.line = line_Gets
           newMatch.start = m.start()
           newMatch.end = m.end()
           newMatch.param = line[(m.start() + 5 ): (m.end()- 1)]

           # print("line :", linenumber)
           print ("WARNING")
           print("at line: ", newMatch.line)
           print('index(start- end) %02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

    print("strcpy(parameter) functions found: "+str(count_strcpy))
    return count_strcpy
```

#### Example 3: File Read
```
def fileread(filePath):
  #file = open(filePath, "r")
  sp.call(['C:/Program Files/Notepad++/notepad++.exe', filePath])
  stderr = sp.STDOUT
  print( stderr )
  return filePath
```

#### Example 4: File Display
```
def fileshow(fileName):
    file = open( fileName, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip()
        print ( line )
    return 0
```

### **Video Tutorial**
---
https://www.youtube.com/########

### **Install**
---
#### Dependencies
The project utilizes Python 3.5 or higher with the PLY package.

#### Instructions
* Download <a href="https://github.com/kensybernadeau/PLP_Titanium/archive/master.zip"> PLP_Titanium </a>
* Install Python 3.4 and the PLY package.
* Run PLP_Titanium/src/Titanium.py

### **Final Report**
---
View <a href="https://#####"> Final Report </a>