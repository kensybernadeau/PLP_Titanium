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

### **Sample Codes**
---
#### Example: 
```
IN-> f = process("<insert source code here>.c")
Code File uploaded
File processed!

IN-> f.evaluate()
WARNING
at line:  6
index(start- end) 00-14: gets(username)
WARNING
at line:  12
index(start- end) 00-14: gets(username)

IN-> f.open()
//Opens Notepad++ on Windows or nano on Linux and MacOS

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
The project utilizes Python 3.x with the PLY package.

#### Instructions
* Install Python 3.x and the PLY package.
* Download <a href="https://github.com/kensybernadeau/PLP_Titanium/archive/master.zip"> PLP_Titanium </a>
* Run ```python PLP_Titanium/src/Titanium.py``` from the system's respective command line interface

### **Final Report**
---
View <a href="https://github.com/kensybernadeau/PLP_Titanium/blob/master/Final%20Report/Final%20Report.md"> Final Report </a>
