### **Introduction**
---
 Secure coding standards provide rules and recommendations to guide the development of secure software systems [1]. These standards ensure that the system will be secure in the developing phase; it also provides a common set of criteria that can be used to measure and evaluate software development efforts and software development process [2]. In the project of Titanium, we design the code to detect the insecure code in a file of C programming language. Since C programming is widely applied in library of Caffe (the programming library for Graphic Processing Unit), our language attaches importance to the protection of software and hardware. By using this language, we use PLY python to design a functional system to implement security checkpoints that would detect code that could lead to a security flaw when the program is being complied.
The motivation for the development of this language is to apply the secure coding standards towards the programmers. Coding standards that most programmers use are incomplete and not security centric. With this language, we can have it running security checks during compilation time such that when it detects any security flaw, the source code ceases to compile and an error is thrown. 
Titanium-Code, the programming language under development, looks to be a tool that regulates and facilitates the prevention of these security flaws. Secure Coding should be something that every programmer should be aware of, thus there should be general standards set to ensure a safe code. For this purpose, this programming language strives to do just that. 
In this report, I will describe, the flowchart of design, language features, the structure of the programming language, development environment, test methodology. At the end, I will conclude this functional language and potential of this project. 

### **Language Development**
The main module of Titanium, titanium.py is the module that takes care of capturing the user input. 
The module passes the user input to the parser, titanium_parser.py, which processes the input with the lexer (titanium_lex.py), and the PLY package. 
After processing the input, the parser then stores the appropriate user input. After we have lexer and parser, we wrote the main program to allow the file (endswith C) and import the parser. 
Then in the implementation.py, we build three functionalities. 
They are the checkpoint method for strcpy(), get(), printf() method in C program. 
When the insecure points are figured out, we have output which shows the number of line where the insecure coding is.

### **Language Tutorial**
---
There are three features about this language. First, it will detect the potential risks. Second it will 
display the location(the No. of line) where the risks occur. At last, the language can provide the 
suggestions that may secure the program. 

To run Titanium language, the user need Python 3.4 and the PLY package installed, then download the PLP_Titanium zip file from github and extract its content. Finally, the user needs to execute PLP_Titanium/titanium.py in order to run the language. 
	This language will serve as a checkpoint before compilation: it will “read” the code and will prevent the code from being compiled if it detects any code fragment that could indicate an eventual security flaw in the system. It should detect vulnerabilities, such as buffer overflow, or a format String Exploit, among others. It should then cancel compilation and warn the user that there is a vulnerability in a specific fragment their code and would indicate how to best deal with the vulnerability. Therefore, the resulting code can have a secure structure, and the user (the programmer) can better understand and begin to code more carefully, avoiding the security risks that could arise.
 

### ****
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





---
#### **Development Environment**
---
The following tools were used to develop Titanium Project:
• Python 3.4 : Language utilized to develop the project
• PLY: Package lex and yacc parsing tools
• PyCharm: IDE utilized to develop the project
• Github: Platform hosting the source code.

### **Test Methodology**
---
yacc.py is used to parse language syntax. Before showing an example, there are a few important bits of background that must be mentioned. 
First, syntaxis usually specified in terms of a BNF grammar. 
For example, if you wanted to parse simple arithmetic expressions, you might first write an unambiguous grammar specification like this:
LR parsing is commonly implemented by shifting grammar symbols onto a stack and looking at the stack and the next input token for patterns that match one of the grammar rules.
When parsing the expression, an underlying state machine and the current input token determine what happens next. 
If the next token looks like part of a valid grammar rule (based on other items on the stack), it is generally shifted onto the stack. If the top of the stack contains a valid right-hand-side of a grammar rule, it is usually "reduced" and the symbols replaced with the symbol on the left-hand-side. When this reduction occurs, the appropriate action is triggered (if defined).
If the input token can't be shifted and the top of stack doesn't match any grammar rules, a syntax error has occurred and the parser must take some kind of recovery step (or bail out). 
A parse is only successful if the parser reaches a state where the symbol stack is empty and there are no more input tokens.
It is important to note that the underlying implementation is built around a large finite-state machine that is encoded in a collection of tables. 
the parser chooses to shift a token onto the stack 
The ply.yacc module implements the parsing component of PLY. The name "yacc" stands for "Yet Another Compiler Compiler" and is borrowed from the Unix tool of the same name.
### **Test Programs**
---

### **Conclusion**
---
The result of this work was a functional language that can detect insecure coding in its early stages. The two proposed main features were successfully implemented and are fully operational. PLP_Titanium’s grammar was designed to be as close as possible to English sentences. This resulted in an intuitive grammar for users who had no prior experience in C programming. The biggest challenge faced during this project was implementing the parse. 
PLP_Titanium has potential to make other aspects of checkpoints. Some of the future features that the team is interested in developing for PLP_Titanium are: multiple file detection, manipulation for insecure C programming. In conclusion, PLP_Titanium has potential to become a powerful tool in the field of software development.


