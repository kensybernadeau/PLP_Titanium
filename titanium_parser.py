import ply.yacc as yacc
import titanium_lexer as Titaniumlex
import os

from implementation import read
from implementation import evaluate
from implementation import fileread
from implementation import fileshow
from implementation import evaluate_overflow
from folder_Checkers import check_this, show_this, showAll, evaluateAll


tokens = Titaniumlex.tokens

global file_path, current_file

files = {}

# ===========================================================================================
# Parsing rules
# ===========================================================================================
def p_help(p):
    '''statement : ID'''

    if p[1].lower() == "help":
        print('''
                TITANIUM HELP

                Process a file or directory:
                <variable name> =  process("/file/path/to/source/")

                Evaluate a file:
                <variable name>.evaluate()

                Open a file:
                <variable name>.open()
                
                Show all available C files in a directory:
                <variable name>.sAll()

                Evaluate all available C files in a directory:
                <variable name>.eALL()
                ''')

def p_statement(p):
    '''statement : fun
                    | assignment
                    | empty
                   '''

    p[0] = p[1]


def p_assignment(p):
    '''assignment : file_assignment
                  | fun_assignment
                    '''
    p[0] = p[1]


def p_fun(p):
    '''fun : fun_no_param
                | fun_single_param
                | fun_without_operation'''

    p[0] = p[1]


def p_fun_without_operation(p):
    '''fun_without_operation : FUN_WITHOUT_OPERATION LP STRING RP '''

    if p[1].lower() == "process".lower():

        print("Code File uploaded")

    p[0] = (p[1],p[3])


def p_fun_no_param(p):
    '''fun_no_param : ID DOT FUN_NO_PARAM LP RP '''

    p[0] = (p[3], p[1])
    global files



    if files.get(p[1]) is None:
        print(p)
        print(p[0])
        print(p[1])
        print(p[2])
        print(p[3])
        print(files)
        print("ID Error here", p[1])

        return p

    if p[3] == 'evaluate':
        if os.path.isdir(files[p[1]]):
           # print(files[p[1]])
           check_this(files[p[1]])

        elif files[p[1]].endswith('.c'):

            evaluate(files[p[1]], 'c')
        # elif files[p[1]].endswith('/'):
        #     print(files[p[1]])
    elif p[3] == "open":
        fileread(files[p[1]])

    elif p[3] == "show":
        if os.path.isdir(files[p[1]]):
            return show_this(files[p[1]])
        fileshow(files[p[1]])

    elif p[3] == 'eAll':
        print("evaluateAll")
        evaluateAll(files[p[1]])
        return

    elif p[3] == 'sAll':
        print("showAll")
        listAll = list()
        showAll(files[p[1]], listAll)
        print(listAll)
        return




        # f = open(duplicatedpath, "r")

#    elif p[3] == 'evaluateOverflow':
#        print("went through!!!!!")
#        if files[p[1]].endswith('.c'):
#            print("C file detected!!")
        #evaluate_overflow(duplicatedpath, 'c')




def p_fun_single_param(p):
    '''fun_single_param : ID DOT FUN_SINGLE_PARAM LP STRING RP'''

    global files
    if files.get(p[1]) is None:
        print("ID Error")
        return p

    duplicatedpath = files[p[1]].copy()

    p[0] = (p[3], p[5])

    if p[3] == 'open':
                print('open')

                fileread(duplicatedpath)

    if p[3] == 'show':
                print('open')

                fileshow(duplicatedpath)





def p_file_assignment(p):
    '''file_assignment : ID EQUALS ID'''
    p[0] = (p[2], p[1], p[3])
    global files

    if files.get(p[3]) is not None:
        files[p[1]] = None
        files.update({p[1]: files[p[3]]})
    else:
        print(' INVALID ID ')




def p_fun_assignment(p):
    '''fun_assignment : ID EQUALS fun_without_operation'''
    p[0] = (p[2], p[1], p[3])
    global files

    if p[3][0] == "process":
        path = p[3][1].replace('"', '')

        if os.path.isdir(path):
            # print(path)
            print("You are about to evaluate the folder instead of one file.")
            files[p[1]] = path
            return

        if not path.endswith(('.txt', '.c')):
            try:
                if (path.endswith('.')):
                    path = path + 'txt'
                else:
                    path = path + '.txt'
                    files[p[1]] = path
                    fileshow(files[p[1]])

            except(Exception):
                try:
                    path = path[:-2]
                    if (path.endswith('.')):
                        path = path + 'c'
                    else:
                        path = path + '.c'
                        files[p[1]] = path

                        # fileshow(files[p[1]])
                except:
                    print("Error: File Not Found!!!!!!")
                    return

        else:
            try:
                print('File processed!')
                files[p[1]] = path

            except:
                print("Error: File Not Found!!!!!")

    else:
        print("Cannot use that method in a assignment")








def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    print("Syntax error: invalid syntax ")
    print("Type \'help\' to print out help")


def getparser():
    return yacc.yacc()


