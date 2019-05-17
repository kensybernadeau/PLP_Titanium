
import os
from implementation import evaluate

def check_this(path):
    print("You are about to evaluate the folder instead of one file.")
    response = input("Want to proceed? Y/N")
    if (response.upper() == "Y"):
        entries = os.listdir(path)
        list_New = list()

        for entry in entries:
            if (entry.endswith('.c')):
                list_New.append(entry)

        print("These are the files under evaluation.")
        print(list_New)
        for e in list_New:
            if path.endswith('/'):
                new_Path = path + e
            else:
                new_Path = path + '/' + e
            print(new_Path)
            evaluate(new_Path, 'c')
    else:
        print("Processing Aborted.")
        return
# This is where processing other files occur.

def show_this(path):
    print("You are about to display all the files and directories in this folder.")
    response = input("Want to proceed? Y/N")
    if (response.upper() == "Y"):
        entries = os.listdir(path)
        list_New = list()
        print("The entries are")
        # print(entries)
        for entry in entries:
            list_New.append(entry)
        print("These are the all the files and directories.")
        for e in list_New:
            new_Path = path + e
            temp = new_Path + '/'
            if (os.path.isdir(temp)):
                print(temp + "  <-- Directory")
            elif(e.endswith(".c")):
                print(new_Path + "  <-- Target File")
            else:
                print(new_Path)
    else:
        print("Processing Aborted.")
        return



def showAll(path, listAll):
    entries = os.listdir(path)
    for entry in entries:
        new_Path = path + entry
        if os.path.isdir(new_Path):
            temp_Path = path + entry + '/'
            # print("The temp path is " + temp_Path)
            showAll(temp_Path, listAll)
        elif new_Path.endswith('.c'):
            listAll.append(new_Path)

def evaluateAll(path):
    listAll = list()
    showAll(path, listAll)
    for e in listAll:
        print()
        print("********************** The file name and location:   " + e + "     *********************************")
        print()
        evaluate(e, 'c')



