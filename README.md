### **Titanium**
---
Titanium is a flexible framework for checking the vulnerabilities of C programming 
language and then providing suggestions of modification. This system has a collection of method that aim 
to find the potential risk of C language across various operating systems, such as Windows, Linux, MacOS.   

### **Background Information**
---
For the novice in C program, there would be some potential security risks that may comprimise a system or a network. 
Especially, if the system is a online platform, these risks may lead to severe securities issues, comprimising confidentiality, availability and integrity of companies.
Titanium, therefore, provides a very accessible way to reminds these novice user of the existence of 
such risk by way of analysing the C source code and throw warnings before the user can compile. 

### **Language Features**
---
There are three features about this language. First, it will detect the potential risks. Second it will 
display the location(the No. of line) where the risks occur. At last, the language can provide the 
suggestions that may secure the program.  

### **Manual Reference**
---
#### Example: 
```
●	Display help:
help
●	Process a given file:
<variable name> = process(“/path/to/file”)
●	Open a given file:
<variable name>.open()
●	Show a file’s content on the terminal:
<variable name>.show()
●	Evaluate the vulnerabilities of the file:
<variable name>.evaluate()
●	Process a given directory:
<variable name> = process(“path/to/directory/”)
●	If we process a directory, the program will show a folder content, indicating the next level of directory and the address of .c files on the terminal:
<variable name>.show()
●	If we process a directory, the system will check all “.c” files and their vulnerabilities.
<variable name>.evaluate()
●	If we process a directory, the program will show all “.c” files under evaluation in this folder.
<variable name>.sAll()
●	If we process a directory, the system will check all “.c” files and show their vulnerabilities.
<variable name>.eAll()
```
### **Video Tutorial**
---
https://www.youtube.com/########

### **The GitPage**
---
https://kensybernadeau.github.io/PLP_Titanium/


### **Install**
---
#### Dependencies
* The project utilizes Python 3.x with the PLY package.
* Anaconda 5.3.0
* backport 0.1.1
#### Instructions
* Install Python 3.x and the PLY package.(Refer to this <a href="https://pythonpedia.com/en/tutorial/10510/python-lex-yacc">page</a> when installing PLY)
* Download <a href="https://github.com/kensybernadeau/PLP_Titanium/archive/master.zip"> PLP_Titanium </a>
* Run ```python PLP_Titanium/src/Titanium.py``` from the system's respective command line interface

### **Final Report**
---
View <a href="https://github.com/kensybernadeau/PLP_Titanium/blob/master/Final%20Report/Final%20Report.md"> Final Report </a>
